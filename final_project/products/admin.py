from django.contrib import admin
from .models import Product, Order

# Register the Product model with the Django admin site
admin.site.register(Product)

# Register the Order model with the Django admin site
admin.site.register(Order)
