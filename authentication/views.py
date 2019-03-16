from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')
