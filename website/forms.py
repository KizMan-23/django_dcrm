from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length="30", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}
    ))
    last_name = forms.CharField(label="", max_length="30", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}
    ))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}
    ))

    class meta:
        model: User
        fields = ('username', 'first_name', 'last_name', 'emial', 'password1', 'password2')