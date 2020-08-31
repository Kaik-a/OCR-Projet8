from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import get_template

from .forms import LoginForm, SubscribeForm


# Create your views here.
def login_user(form: LoginForm, request):
    username = form.data.get('login')
    password = form.data.get('password')

    if username and password:
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'form': form})


def get_user_info(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return login_user(form, request)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.data.get('login'),
                password=form.data.get('password')
            )
            form_connect = LoginForm()

            return render(request, 'login.html', {'form': form_connect})
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})


def sign_out(request):
    logout(request)

    return render(request, 'home.html')
