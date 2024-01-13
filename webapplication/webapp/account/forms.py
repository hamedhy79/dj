from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterationForms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your  Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This Username Already Is Exist')
        return username

    @property
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email Already Is Exist')
        return email

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('This Password Not Match')


# login
class UserLoginForms(forms.Form):
    username = forms.CharField(label="username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(label="username", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
