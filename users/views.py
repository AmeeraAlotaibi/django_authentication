from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, authenticate
# Create your views here.


def register_view(request):
    form = RegistrationForm()
    print("Here")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("register-success")

    context = {
        "form": form
    }
    return render(request, 'register.html', context)


def get_home(request):
    return render(request, 'base.html')


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("register-success")

    context = {
        "form": form,
    }

    return render(request, 'login.html', context)
