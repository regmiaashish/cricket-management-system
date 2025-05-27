from django.urls import path
from store.views import shop, eachproduct, add_to_cart, view_cart, remove_from_cart, product_list, add_product, edit_product, delete_product, checkout_view ,initiate_payment, verify_payment, download_receipt, complete_order

urlpatterns = [
    path('',shop, name='shopview'),
    #Product CRUD
    path('product',product_list, name='product_list'), #R
    path('product/add/', add_product, name='add_product'),#C
    path('product/edit/<id>', edit_product, name='edit_product'),#U
    path('product/delete/<id>', delete_product, name='delete_product'),#D
    
    
    path('productlist/<id>',eachproduct, name='eachproduct'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    
    
    path('checkout/', checkout_view, name='checkout'),
    path('payment/initiate/<int:order_id>/', initiate_payment, name='initiate_payment'),
    path('payment/verify/', verify_payment, name='verify_payment'),

    # urls.py
    path('orders/<int:order_id>/receipt/', download_receipt, name='download_receipt'),
    path('complete-order/', complete_order, name='complete_order'),
]