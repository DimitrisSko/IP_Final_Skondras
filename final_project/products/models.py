from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Model to represent a product
class Product(models.Model):
    # Title of the product with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # Author or creator of the product with a maximum length of 200 characters
    author = models.CharField(max_length=200)
    
    # Description of the product with a maximum length of 500 characters; can be blank
    description = models.CharField(max_length=500, default=None)
    
    # Price of the product; can be null or blank
    price = models.FloatField(null=True, blank=True)
    
    # URL for the product image; allows up to 2083 characters, default is False (though it should probably be an empty string)
    image_url = models.CharField(max_length=2083, default='')
    
    # Availability status of the product
    product_available = models.BooleanField(default=False)

    # Return the title of the product when the model instance is printed
    def __str__(self):
        return self.title

# Model to represent an order
class Order(models.Model):
    # Foreign key relationship to the Product model; allows null or blank values and deletes the order if the associated product is deleted
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    
    # Timestamp of when the order was created, automatically set when an order is created
    created = models.DateTimeField(auto_now_add=True)

    # Return the title of the associated product when the model instance is printed
    def __str__(self):
        return self.product.title
