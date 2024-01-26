from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='Firstname', max_length=100)
    last_name = forms.CharField(label='Lastname', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


