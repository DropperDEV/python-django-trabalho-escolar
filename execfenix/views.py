from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.

def home(request):
    return render(request,'home.html')
# inserção de dados form
def create(request):
    return render(request,'create.html')

# autenticação de dados do form
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha diferentes!!'
    else:
        user = User.objects.create_user(request.POST['user'],request.POST['email'],request.POST['password'])
        user.save()
        user.user_permissions.add(25)
        data['msg'] = 'Cadastro com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)
#   Login
def log(request):
    return render(request,'log.html')

# processo login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha incorreto'
        data['class'] = 'alert-danger'
        return render(request,'log.html',data)

# PAG INTERNO
def dashboard(request):
    return render(request, 'dashboard/home.html')

# SAIR
def logouts(request):
    logout(request)
    return redirect('/log/')

# Form Mudar Senha
def csenha(request):
    return render(request,'csenha.html')

# Mudar senha
def ChangePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/log/')
