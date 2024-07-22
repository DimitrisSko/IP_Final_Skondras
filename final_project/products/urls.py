from django.urls import path
from .views import ProductsListView, ProductsDetailView, ProductCheckoutView, paymentComplete, SearchResultsListView

urlpatterns = [
    # URL pattern for the home page which lists all products
    path('', ProductsListView.as_view(), name='list'),

    # URL pattern for product details view; expects an integer primary key (pk)
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail'),

    # URL pattern for the product checkout page; expects an integer primary key (pk)
    path('<int:pk>/checkout/', ProductCheckoutView.as_view(), name='checkout'),

    # URL pattern for handling payment completion
    path('complete/', paymentComplete, name='complete'),

    # URL pattern for search results page
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
