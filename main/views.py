import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.forms import Product
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.http import JsonResponse

@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'nama': request.user.username,
        'items': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'product_list.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:product_list'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def registrasi(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'registrasi.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:product_list")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def product_management(request):
    products = Product.objects.filter(user=request.user)
    context = {'products': products}
    return render(request, 'manage_products.html', context)

def add_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.quantity += 1
        product.save()
        messages.success(request, 'Product quantity increased.')
    return redirect('main:product_management')

def subtract_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if product.quantity > 0:
            product.quantity -= 1
            product.save()
            messages.success(request, 'Product quantity decreased.')
        else:
            messages.warning(request, 'Product quantity cannot be negative.')
    return redirect('main:product_management')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
    return redirect('main:product_management')

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        image = request.POST.get("image")
        user = request.user

        new_product = Product(name=name, quantity=quantity, description=description, image=image, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request, id):
    product = Product.objects.get(pk=id)
    product.delete
    return HttpResponseRedirect(reverse('main:product_list'))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            name = data["name"],
            quantity = int(data["quantity"]),
            description = data["description"],
            image = data["image"],
            user = request.user,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)