from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            passWord = form.clean_password2()
            print(passWord)
            messages.success(request, f'Welcome {userName}, you are logged in successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"form": form})


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

