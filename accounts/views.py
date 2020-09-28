from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, SubscribeForm


def login_user(request, form: LoginForm):
    username = form.data.get('login')
    password = form.data.get('password')
    import pdb;pdb.set_trace()
    if username and password:
        user: User = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            messages.add_message(
                request,
                25,
                f"Bonjour {user.first_name}! Vous êtes maintenant connecté"
            )
            return redirect(
                reverse('accounts:user_account')
            )
        else:
            messages.add_message(
                request,
                40,
                'Aucun compte recensé avec cette combinaison. Votre email ou mot de '
                'passe sont peut être incorrects?'
            )
            return render(request, 'login.html', {'form': form})


def get_user_info(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return login_user(request, form)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(
                    username=form.data.get('login'),
                    password=form.data.get('password'),
                    first_name=form.data.get('first_name'),
                    last_name=form.data.get('last_name'),
                    email=form.data.get('email')
                )
            except IntegrityError as e:
                print(e)
            form_connect = LoginForm()

            return redirect(reverse('accounts:login'), form=form_connect)
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})


@login_required
def sign_out(request):
    logout(request)

    messages.add_message(
        request,
        25,
        'Au revoir!'
    )
    return redirect(reverse('home'))


@login_required
def user_account(request):
    return render(request, "user_account.html")
