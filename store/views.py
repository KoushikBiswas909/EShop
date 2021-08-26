from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.product import Category

# Create your views here.
def index(request):

    products = Product.get_all_products();
    categories = Category.get_all_categories()
    categoryID = request.GET['category']
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)
    #return render(request, 'index.html', {'products': products})
