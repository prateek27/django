from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username = forms.CharField(initial = "Enter Your UserName", required = True)
    password = forms.CharField(initial="Enter Password", required = True)
