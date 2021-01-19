from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# Create your views here.
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('website:home')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout')

    return render(request, 'users/logout.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
