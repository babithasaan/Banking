from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def index(request):
    return render(request, 'base.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info("You are Successfully Logged In")
            return redirect('index')
        else:
            messages.info("Invalid Username and Password")
            return redirect('login')

    return render(request, "login.html", {})


def registerin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        cpassword = request.POST['ConfirmPassword']
        if password == cpassword:
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, )
                user.save();
                print("User Created Successfully")
                return redirect('login')

        else:
            print("Incorrect Password")
            return redirect('register')

        return redirect('/')
    return render(request, "register.html")


def newform(request):
    return render(request, 'newpage.html', {})


def logout(request):
    auth.logout(request)
    return redirect('/')
