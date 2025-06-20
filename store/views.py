from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib import messages
from django.db import transaction
from tournament.middlewares import auth, guest, staff
from store.models import Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from store.forms import ProductForm
from decimal import Decimal
import requests
from xhtml2pdf import pisa
from django.template.loader import get_template


# Create your views here.


def shop(request):
    list = Product.objects.all()
    content = {"data": list}
    return render(request, "store/shop.html", content)


def eachproduct(request, id):
    product = Product.objects.get(id=id)
    sizes = ["XS", "S", "M", "L", "XL"]
    context = {
        "data": product,
        "sizes": sizes,
    }
    return render(request, "store/product_detail.html", context)




@auth
def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.subtotal() for item in cart_items)
    else:
        cart_items = []
        total = 0

    context = {
        "cart_items": cart_items,
        "total": total,
    }
    return render(request, "store/cart.html", context)



@auth # Use your custom auth decorator here
@transaction.atomic
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        size = request.POST.get("size")
        quantity = int(request.POST.get("quantity", 1))

        if quantity > product.stock:
            
            return redirect("view_cart")

        with transaction.atomic():
            product.stock -= quantity
            product.save()

            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product,
                size=size,
                defaults={"quantity": quantity},
            )

            if not created:
                cart_item.quantity += quantity
                cart_item.save()

        return redirect("view_cart")

    return redirect("shopview")


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect("view_cart")


@auth
def product_list(request):
    content = {"data": Product.objects.all}
    return render(request, "store/manage_product.html", content)


@auth
@staff
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "store/add_product.html", info)


@auth
@staff
def edit_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            return form.errors

    context = {"data": product, "form": form}
    return render(request, "store/edit_product.html", context)


def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect("product_list")


##Checkout

@auth
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return JsonResponse({"error": "Cart is empty."})

    total = sum(item.subtotal() for item in cart_items)

    order = Order.objects.create(
        user=request.user, total_amount=Decimal(total), is_paid=False
    )
    
        # ✅ Save OrderItems before redirecting to Khalti
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            size=item.size,
            quantity=item.quantity,
            price=item.product.price,
        )

    return redirect("initiate_payment", order_id=order.id)

@transaction.atomic()
def initiate_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    payload = {
        "return_url": "http://localhost:8000/store/payment/verify/",
        "website_url": "http://localhost:8000/",
        "amount": int(order.total_amount * 100),
        "purchase_order_id": str(order.id),
        "purchase_order_name": "Jersey Order",
        "customer_info": {
            "name": request.user.get_full_name() or request.user.username,
            "email": request.user.email,
            "phone": "9800000000",
        },
    }

    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://a.khalti.com/api/v2/epayment/initiate/", json=payload, headers=headers
    )
    data = response.json()

    if response.status_code == 200 and data.get("payment_url"):
        return redirect(data["payment_url"])
    else:
        return render(
            request,
            "store/payment_failed.html",
            {"error": data.get("detail", "Failed to initiate payment")},
        )


@transaction.atomic()
def verify_payment(request):
    pidx = request.GET.get("pidx")
    order_id = request.GET.get("purchase_order_id")

    if not pidx or not order_id:
        return render(request, "store/payment_failed.html", {
            "error": "Missing required payment information."
        })

    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://a.khalti.com/api/v2/epayment/lookup/",
        json={"pidx": pidx},
        headers=headers,
    )

    data = response.json()

    if data.get("status") == "Completed":
        order = get_object_or_404(Order, id=order_id)
        order.is_paid = True
        order.khalti_transaction_id = data.get("transaction_id")
        order.save()

        # ✅ Clear cart only if user is logged in
        if order.user:
            CartItem.objects.filter(user=order.user).delete()


        return render(request, "store/payment_success.html", {"order": order})

    return render(request, "store/payment_failed.html", {
        "error": data.get("message", "Payment Failed."),
    })
    
    
    

def download_receipt(request, order_id):

    order = Order.objects.get(id=order_id)

    template_path = 'store/order_receipt.html'
    context = {'order': order}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_order_{order_id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("PDF generation failed", status=500)

    return response

