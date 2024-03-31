from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from . models import *
from .forms import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout


class IndexView(APIView):
    def get(self, request):
        products = InventoryItem.objects.all()
        form = LoginUserForm()
        return render(request, 'warehouse_management/index.html',
                      {'products': products, 'form': form, 'title': 'Вход в систему'})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return redirect('index')


class Logout(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('index')


def main(request):
    if not request.user.is_anonymous:
        products = InventoryItem.objects.all()
        categories = Category.objects.all()
        warehouses = Warehouse.objects.all()
        data = {
            'products': products,
            'categories': categories,
            'warehouses': warehouses
        }
        return render(request, 'warehouse_management/main.html', context=data)


def modal(request):
    form = LoginUserForm()
    return render(request, 'warehouse_management/modal.html', {'form': form})
