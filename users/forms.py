from socket import fromshare
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
