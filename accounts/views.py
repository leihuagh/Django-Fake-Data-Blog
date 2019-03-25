from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('/login')
        else:
            form = RegisterForm()

    return render(request, 'register.html', context)
