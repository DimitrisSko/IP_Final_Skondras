from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product, Order
from django.urls import reverse_lazy
from django.db.models import Q  # Import Q for complex queries
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# View to list all products
class ProductsListView(ListView):
    model = Product
    template_name = 'list.html'  # Template to render the product list

# View to display details of a single product
class ProductsDetailView(DetailView):
    model = Product
    template_name = 'detail.html'  # Template to render the product details

# View to display search results for products
class SearchResultsListView(ListView):
    model = Product
    template_name = 'search_results.html'  # Template to render search results

    # Override the default queryset to filter based on search query
    def get_queryset(self):
        query = self.request.GET.get('q')
        # Filter products where title or author contains the query string
        return Product.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

# View to handle product checkout, requires user to be logged in
class ProductCheckoutView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'checkout.html'  # Template to render the checkout page
    login_url = 'login'  # Redirect to login if the user is not authenticated

# View to handle the completion of a payment
def paymentComplete(request):
    # Parse the JSON body of the request
    body = json.loads(request.body)
    print('BODY:', body)  # Debugging: print the body of the request
    # Get the product object based on the product ID from the request
    product = Product.objects.get(id=body['productId'])
    # Create a new order for the product
    Order.objects.create(
        product=product
    )
    # Respond with a JSON message indicating payment completion
    return JsonResponse('Payment completed!', safe=False)
