from allauth.account.views import LoginView, SignupView
from allauth.account.forms import LoginForm
from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import CustomSignupForm


class CustomLoginView(LoginView):
    template_name = "home/index.html"
    success_url = reverse_lazy("index")

    def form_invalid(self, form):
        """
        If login fails, render index.html with login_form errors
        and also show signup_form (empty).
        """
        signup_form = CustomSignupForm()
        return render(self.request, "home/index.html", {
            "login_form": form,
            "signup_form": signup_form,
            "show_login_modal": True,  # flag to reopen modal in template
        })


class CustomSignupView(SignupView):
    template_name = "home/index.html"
    success_url = reverse_lazy("index")  
    
    def form_invalid(self, form):
        """
        If signup fails, render index.html with signup_form errors
        and also show login_form (empty).
        """
        login_form = LoginForm()
        return render(self.request, "home/index.html", {
            "signup_form": form,        # show signup errors
            "login_form": login_form,   # empty login form
            "show_register_modal": True # flag to reopen modal
        })

      
