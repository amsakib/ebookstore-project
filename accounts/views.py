from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        # sign up the user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                print("OK I AM HERE")
                return render(request, 'accounts/signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request, 'ebook/home.html', {'success': 'You are successfully registered and logged in!'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords aren\'t matched!'})
    else:
        # user wants to sign up
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # login user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'ebook/home.html', {'success': 'You are successfully logged in!'})
        else:
            return render(request, 'accounts/login.html', {'error': 'Username/Password doesn\'t match'})
    else:
        # user wants to login
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('home')
