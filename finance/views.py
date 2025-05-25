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

@login_required(login_url="log")
def get_dr(request):
    return render(request, 'show.html')

@login_required(login_url='log')
def show_doxod(request):
    doxod = Doxod.objects.filter(user=request.user)
    search = request.POST.get('search')
    date = request.POST.get('date')

    if search:
        doxod = doxod.filter(name__icontains=search)
    if date:
        doxod = doxod.filter(created_at__date=date)

    return render(request, 'showdoxod.html', {'d': doxod})


@login_required(login_url='log')
def add_doxod(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        if name and amount:
            Doxod.objects.create(name=name, amount=amount, user=request.user)
            return redirect('showd')
    return render(request, 'adddoxod.html')

@login_required(login_url='log')
def update_doxod(request, id):
    doxod = get_object_or_404(Doxod, id=id, user=request.user)
    if request.method == 'POST':
        doxod.name = request.POST.get('name')
        doxod.amount = request.POST.get('amount')
        doxod.save()
        return redirect('showd')
    return render(request, 'update_doxod.html', {'doxod': doxod})

@login_required(login_url='log')
def delete_doxod(request, id):
    doxod = get_object_or_404(Doxod, id=id, user=request.user)
    doxod.delete()
    return redirect('showd')



@login_required(login_url='log')
def show_rasxod(request):
    rasxod = Rasxod.objects.filter(user=request.user)
    search = request.POST.get('search')
    date = request.POST.get('date')

    if search:
        rasxod = rasxod.filter(name__icontains=search)
    if date:
        rasxod = rasxod.filter(created_at__date=date)

    return render(request, 'showrasxod.html', {'r': rasxod})

@login_required(login_url='log')
def add_rasxod(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        if name and amount:
            Rasxod.objects.create(name=name, amount=amount, user=request.user)
            return redirect('showr')
    return render(request, 'addrasxod.html')

@login_required(login_url='log')
def update_rasxod(request, id):
    rasxod = get_object_or_404(Rasxod, id=id, user=request.user)
    if request.method == 'POST':
        rasxod.name = request.POST.get('name')
        rasxod.amount = request.POST.get('amount')
        rasxod.save()
        return redirect('showr')
    return render(request, 'update_rasxod.html', {'rasxod': rasxod})


@login_required(login_url='log')
def delete_rasxod(request, id):
    rasxod = get_object_or_404(Rasxod, id=id, user=request.user)
    rasxod.delete()
    return redirect('showr')