import random
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

from .forms import CustomerForm, SellerForm, SaleForm, ProductForm
from .models import Customer, Seller, Sale, Product


def customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()

    customers = Customer.objects.all()
    return render(request, 'customers_list.html', {'customers': customers, 'form': form})


def sellers(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellers')
    else:
        form = SellerForm()

    sellers = Seller.objects.all()
    return render(request, 'sellers_list.html', {'sellers': sellers, 'form': form})


def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products, 'form': form})


def sales(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales')
    else:
        form = SaleForm()

    sales = Sale.objects.all()
    return render(request, 'sales_list.html', {'sales': sales, 'form': form})


def delete_customer_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customers')

def delete_seller_view(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    seller.delete()
    return redirect('sellers')

def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')

def delete_sale_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    return redirect('sales')