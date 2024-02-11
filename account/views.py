from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userlogin(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:main')
    if request.method == 'POST':
        Username = request.POST.get("username")
        Password = request.POST.get("pass")
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('home_app:main')

    return render(request, 'account/login.html', context={})



def Register(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('home_app:main')

    if request.method == 'POST':
        Username = request.POST.get("username")
        Email = request.POST.get("email")
        Pass = request.POST.get("pass1")
        ConfrimPass = request.POST.get("pass2")

        if Pass != ConfrimPass:
            context['errors'].append('passwords are not same')
            return render(request, 'account/register.html', context)

        '''if User.objects.get(username=Username):
            context['errors'].append('username is already exists')
            return render(request, 'account/register.html', context)'''

        user = User.objects.create(username=Username, password=Pass, email=Email)
        login(request, user)
        return redirect('home_app:main')

    return render(request, 'account/register.html', {})



def userlogout(request):
    logout(request)
    return redirect('home_app:main')