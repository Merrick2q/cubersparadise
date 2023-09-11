from django.shortcuts import render
from .models import Product

product_name = 'Mscube MS3X'
product_quantity = '50'
product_description = 'Puzzle rubik flagship oleh Mscube'

def product_list(request):
    return render(request, 'product_list.html', {'name' : product_name, 'quantity' : product_quantity, 'description' : product_description})
