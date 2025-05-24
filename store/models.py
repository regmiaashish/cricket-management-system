from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name="Stock")
    image = models.ImageField(upload_to='jerseys/', blank=True, null=True, verbose_name="Image")
    is_available = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
    
    
class CartItem(models.Model):
    SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, verbose_name="Size")

    def subtotal(self):
        return self.product.price * self.quantity

 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    khalti_transaction_id = models.CharField(max_length=100, blank=True, null=True)
     
  
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=3)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price
