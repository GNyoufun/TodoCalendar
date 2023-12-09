from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("pass")
            login(request, user)
            return redirect("home")
        else:
            print("fail")
            messages.success(request, "The username or password is incorrect, Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html')