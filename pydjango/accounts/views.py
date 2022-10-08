from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken!")
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered!")
                return redirect("register")

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.info(request, "Registration successful! Please Login!")
                return redirect("login")
        else:
            messages.info(request, "Passwords not matching!")
            return redirect("register")

    else:
        return render(request, "register.html")


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect("login")
    else:
        return render(request, "login.html")
