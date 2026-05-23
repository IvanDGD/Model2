from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('sellers/', views.sellers, name='sellers'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
    path('customers/delete/<uuid:pk>/', views.delete_customer_view, name='delete_customer'),
    path('sellers/delete/<uuid:pk>/', views.delete_seller_view, name='delete_seller'),
    path('products/delete/<uuid:pk>/', views.delete_product_view, name='delete_product'),
    path('sales/delete/<uuid:pk>/', views.delete_sale_view, name='delete_sale'),
]