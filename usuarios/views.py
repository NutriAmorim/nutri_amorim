from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')


def cadastro_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('username', '').strip()
        senha = request.POST.get('senha', '').strip()
        email = request.POST.get('email', '').strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        user.save()

        messages.success(
            request,
            f'Cadastro feito com sucesso! Bem-vindo, {username}!'
        )
        login(request, user)
        return redirect('home')


def painel_view(request):
    return render(request, 'usuarios/painel.html')


def plataforma_view(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma')
    return HttpResponse('Você precisa estar logado')


def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('home')


def home(request):
    return render(request, 'home.html')
