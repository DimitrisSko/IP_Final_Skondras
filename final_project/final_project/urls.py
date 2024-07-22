from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pattern for the Django admin interface
    path('admin/', admin.site.urls),

    # Include URLs from the 'products' app
    path('', include('products.urls')),

    # Include URLs from the 'accounts' app
    path('', include("accounts.urls")), 

    # Include default authentication URLs from Django's built-in auth system
    path('accounts/', include("django.contrib.auth.urls")), # Handles login, logout, password change, etc.

    # URL pattern for logging out of the application
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
