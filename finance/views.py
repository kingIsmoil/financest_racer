from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Doxod, Rasxod
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username and password == password2:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
            return redirect('log')
        return redirect('reg')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dr')
        return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

