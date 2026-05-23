from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('books/', views.book_list, name="books"),
    path('readers/', views.reader_list, name="readers"),
    path('details/<str:id>/', views.reader_details, name="details"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('book/<str:book_id>/take/', views.take_book, name='take_book'),
]