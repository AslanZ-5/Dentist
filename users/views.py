from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


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
    return render(request, 'users/logout.html')
