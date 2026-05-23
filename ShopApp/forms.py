from django import forms
from .models import Customer, Seller, Sale, Product

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'phone', 'email', 'hire_date', 'position']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'seller']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'seller', 'product', 'quantity', 'total_amount']