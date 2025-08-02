from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length="30", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}
    ))
    last_name = forms.CharField(label="", max_length="30", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}
    ))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}
    ))

    class Meta:
        model =  User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer digits and @/./+/-/_ only. </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t contain personal information</li><li>Your password must contain at least 8 characters</li>' \
                                            '<li>Your password can\'t be common words</li><li>Your password can\'t be entirely numeric</li>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as above to confirm your password. </small></span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    last_name = forms.CharField(max_length=30, label='Last Name', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.CharField(max_length=40, label='Email Address', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    phone = forms.CharField(max_length=30, label='Phone Number', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    address = forms.CharField(max_length=50, label='Address', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    city = forms.CharField(max_length=30, label='City', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    state = forms.CharField(max_length=30, label='State', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))
    zipcode = forms.CharField(max_length=30, label='ZipCode', required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Record
        exclude = ("user",) #or use fields as in SignUpForm
    
