from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from .models import CustomUser, Document

class MyRegForm(UserCreationForm):
    username=forms.CharField(label='Enter username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter username',
            'onblur':'checkUser(this.value)'
        }))
    first_name = forms.CharField(label='Enter your first name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your first name'
        }))
    last_name = forms.CharField(label='Enter your last name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your last name'
        }))
    email = forms.CharField(label='Enter your email*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your email'
        }))
    email = forms.CharField(label='Enter your email*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your email'
        }))
    mobile=forms.CharField(label='Enter your contact number*', widget=forms.NumberInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your contact number'
        }))
    password1 = forms.CharField(label='Enter your password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your password'
        }))
    password2 = forms.CharField(label='Enter your confirm password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your confirm password'
        }))
    class Meta:
        model=CustomUser
        fields=['username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter username'
        }))
    password = forms.CharField(label='Enter your password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your password'
        }))
class MychangePwdForm(PasswordChangeForm):
    old_password = forms.CharField(label='Enter your current password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your current password'
        }))
    new_password1 = forms.CharField(label='Enter your new password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your new password'
        }))
    new_password2 = forms.CharField(label='Enter your confirm password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your confirm password'
        }))

class MyUserChangeFrm(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Enter your first name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your first name'
        }))
    last_name = forms.CharField(label='Enter your last name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your last name'
        }))
    email = forms.CharField(label='Enter your email*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your email'
        }))
    email = forms.CharField(label='Enter your email*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your email'
        }))
    mobile = forms.CharField(label='Enter your contact number*', widget=forms.NumberInput(
        attrs={
            'class': 'form-control border-0 p-4 mb-3',
            'placeholder': 'Enter your contact number'
        }))
    class Meta:
        model=CustomUser
        fields=['first_name', 'last_name', 'email', 'mobile']

class DocumentUploadFrm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['title', 'file']
