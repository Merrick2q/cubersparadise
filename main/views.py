# views.py
from django.shortcuts import render
from .models import Item

def product_list(request):
    items = Item.objects.all()
    return render(request, 'product_list.html', {'items': items})
