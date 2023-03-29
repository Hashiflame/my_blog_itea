from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserForm, LoginForm


def register(request):
    form = UserForm()
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            login(request, new_user)
            messages.add_message(
                request, messages.SUCCESS, 'You have been registered successfully!!!)))'
            )
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'You logged in'
                )
                return redirect('home')

            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'User not found'
                )
                return redirect('login')


    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')