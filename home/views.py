from allauth.account.forms import LoginForm, SignupForm
from django.shortcuts import render


def index(request):
    context = {
        'login_form': LoginForm(),
        'signup_form': SignupForm(),
    }
    
    return render(request, 'home/index.html', context)
