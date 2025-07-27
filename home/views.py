from django.shortcuts import render
from allauth.account.forms import LoginForm
from accounts.forms import CustomSignupForm

def index(request):
    return render(
        request,
        "home/index.html",
        {
            "login_form": LoginForm(),
            "signup_form": CustomSignupForm(),
        },
    )

