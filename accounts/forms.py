from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address_line_1 = forms.CharField(max_length=255, required=False)
    address_line_2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    postcode = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def signup(self, request, user):
        """
        Called automatically by allauth after the user is created.
        """
        profile = user.profile
        profile.phone_number = self.cleaned_data.get("phone_number")
        profile.address_line_1 = self.cleaned_data.get("address_line_1")
        profile.address_line_2 = self.cleaned_data.get("address_line_2")
        profile.city = self.cleaned_data.get("city")
        profile.postcode = self.cleaned_data.get("postcode")
        profile.save()
        return user
