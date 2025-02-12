from django.urls import path
from store.views import shop, productlist 

urlpatterns = [
    path('',shop, name='shopview'),
    path('productlist/<id>',productlist, name='shopview'),
    
]