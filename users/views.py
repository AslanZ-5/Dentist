from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import ProfileForm, UserProfileForm


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
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


def profile(request):
    if request.method == 'POST':
        form_a = UserProfileForm(request.POST,instance=request.user)
        form_b = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form_a.is_valid() and form_b.is_valid():
            form_a.save()
            form_b.save()
            return redirect('profile')
    else:
        form_a = UserProfileForm(instance=request.user)
        form_b = ProfileForm(instance=request.user.profile)



    return render(request, 'users/profile.html', {"form_a": form_a, "form_b": form_b})
