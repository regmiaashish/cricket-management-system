from django.shortcuts import render
from store.models import Product

# Create your views here.

def shop(request):
    list = Product.objects.all()
    content = {'data':list}
    return render(request, 'store/shop.html', content)

def productlist(request, id):
    pass
