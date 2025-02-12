from django.db import models

# Create your models here.
class Product(models.Model):
    SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
]
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name="Stock")
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, verbose_name="Size")
    image = models.ImageField(upload_to='jerseys/', blank=True, null=True, verbose_name="Image")
    is_available = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
      
  