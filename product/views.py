from django.shortcuts import render
from django.urls import reverse_lazy

from . import models
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = models.Product
    template_name = 'product/products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product/product.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = models.Product
    fields = ('name', 'description', 'price', 'stock_count', "sku", "slug")
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list')
