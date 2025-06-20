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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget_attrs['class'] = 'form-control',
        self.fields['username'].widget_attrs['placeholder'] = 'User Name',
        self.fields['username'].label = "",
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer digits and @/./+/-/_ only. </small></span>'

        self.fields['password1'].widget_attrs['class'] = 'form-control',
        self.fields['password1'].widget_attrs['placeholder'] = 'Password',
        self.fields['password1'].label = "",
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t contain personal information</li><li>Your password must contain at least 8 characters</li>' \
                                            '<li>Your password can\'t be common words</li><li>Your password can\'t be entirely numeric</li>'

        self.fields['password2'].widget_attrs['class'] = 'form-control',
        self.fields['password2'].widget_attrs['placeholder'] = 'Confirm Password',
        self.fields['password2'].label = "",
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as above to confirm your password. </small></span>'