from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, "login.html", {"form": form})

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            return render(
                request,
                "login.html",
                {"form": form, "error": "Invalid email or password"},
            )

        return redirect("/")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if not form.is_valid():
            return render(request, "sign_up.html", {"form": form})

        username = form.cleaned_data["username"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirm_password = form.cleaned_data["confirm_password"]

        if password != confirm_password:
            return render(
                request,
                "sign_up.html",
                {"form": form, "error": "Passwords do not match"},
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        return render(
            request,
            "sign_up_success.html",
            {"user": {"firstname": first_name, "lastname": last_name, "email": email}},
        )

    form = SignUpForm()

    return render(request, "sign_up.html", {"form": form})
