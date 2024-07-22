from django.apps import AppConfig

class ProductsConfig(AppConfig):
    # Default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the application
    name = 'products'

