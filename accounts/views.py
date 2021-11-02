from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            print('authenticate')
            return redirect('index')
        else:
            print('Ooops!!')
    return render(request, 'accounts/login.html')
