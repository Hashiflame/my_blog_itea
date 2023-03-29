from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserForm


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
    form = UserForm()

    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                form.cleaned_data['username'],
                form.cleaned_data['password']
            )
    context = {
        'form': form
    }
    return render(requet, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')