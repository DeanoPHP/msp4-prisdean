from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(required=False)
    address_line_1 = forms.CharField(required=False)
    address_line_2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    postcode = forms.CharField(required=False)

    def signup(self, request, user):
        # Save profile data
        user.profile.phone_number = self.cleaned_data.get('phone_number')
        user.profile.address_line_1 = self.cleaned_data.get('address_line_1')
        user.profile.address_line_2 = self.cleaned_data.get('address_line_2')
        user.profile.city = self.cleaned_data.get('city')
        user.profile.postcode = self.cleaned_data.get('postcode')
        user.profile.save()
        return user
