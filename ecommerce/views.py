from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "name": "Home page",
        "content": "This is the home page"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "PREMIUM CONTENT"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "name": "About page",
        "content": "This is the about page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "name": "Contact page",
        "content": "This is the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

""" Controlador para el login """
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in...")
    print("1", request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print("2", request.user.is_authenticated)
        if user is not None:
            # print("3", request.user.is_authenticated)
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)

""" Controlador para el registro """

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
