import random
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group

from .forms import RegistrationForm, LoginForm
from .models import Book, Reader


def is_reader(user):
    return user.groups.filter(name='Читатели').exists() or user.is_superuser

def book_list(request):
    status_filter = request.GET.get('status', 'all')
    books = Book.objects.filter(is_taken=False) if status_filter == 'available' else Book.objects.all()
    is_reader = False
    if request.user.is_authenticated:
        is_reader = request.user.groups.filter(name='Читатели').exists() or request.user.is_superuser

    context = {
        'books': books,
        'current_filter': status_filter,
        'user_can_take': is_reader
    }
    return render(request, 'book_list.html', context)



def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'reader_list.html', {'readers': readers})


def reader_details(request, id):
    readers = Reader.objects.all()
    reader = readers.get(id=id)
    return render(request, 'reader_details.html', {'reader': reader})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['name'],
                last_name=form.cleaned_data['surname']
            )
            readers_group, created = Group.objects.get_or_create(name='Читатели')
            user.groups.add(readers_group)

            reader = form.save(commit=False)
            reader.save()

            auth_login(request, user)
            return redirect("books")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("books")
            else:
                error_message = "Неверный Email или пароль"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def take_book(request, book_id):
    if request.method == 'POST':
        books = Book.objects.all()
        book = books.get(id=book_id)
        if not book.is_taken:
            try:
                current_reader = Reader.objects.get(email=request.user.email)
                book.is_taken = True
                book.reader = current_reader
                book.save()
            except Reader.DoesNotExist:
                return HttpResponse("Профиль читателя не найден для вашего аккаунта.", status=400)
    return redirect('books')