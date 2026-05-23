from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('sellers/', views.sellers, name='sellers'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
]