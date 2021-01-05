from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from.models.category import Category
# Create your views here.


def index(request):
    products = Product.get_all_products()
    category = Category.get_all_category()

    context = {
        'products': products,
        'category': category
    }
    return render(request, 'store/index.html', context)
