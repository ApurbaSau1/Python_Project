from django import forms
from . models import CustomUser, Contact
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm, UserChangeForm

class MyRegForm(UserCreationForm):
    username=forms.CharField(label='Enter User Name',
                             widget=forms.TextInput(
                             attrs={'placeholder':'Enter UserName','class':'form-control'}
                             ))
    first_name=forms.CharField(label='Enter First Name',
                             widget=forms.TextInput(
                             attrs={'placeholder':'Enter First Name','class':'form-control'}
                             ))
    last_name=forms.CharField(label='Enter Last Name',
                             widget=forms.TextInput(
                             attrs={'placeholder':'Enter Last Name','class':'form-control'}
                             ))
    email=forms.CharField(label='Enter Email',
                             widget=forms.EmailInput(
                             attrs={'placeholder':'Enter Email','class':'form-control'}
                             ))
    contact_no=forms.CharField(label='Enter Contact Number',
                             widget=forms.NumberInput(
                             attrs={'placeholder':'Enter Contact Number','class':'form-control'}
                             ))
    password1=forms.CharField(label='Enter Password',
                             widget=forms.PasswordInput(
                             attrs={'placeholder':'Enter Password','class':'form-control'}
                             ))
    password2=forms.CharField(label='Confirm Password',
                             widget=forms.PasswordInput(
                             attrs={'placeholder':'Confirm Password','class':'form-control'}
                             ))
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','contact_no']

class MyLogForm(AuthenticationForm):
    username=forms.CharField(label='Enter User Name',widget=forms.TextInput(attrs={'placeholder':'Enter User Name','class':'form-control'}))

    password=forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password','class':'form-control password'}))

class MyContactForm(forms.ModelForm):
    
    name=forms.CharField(label='Enter User Name',widget=forms.TextInput(attrs={'placeholder':'Enter Your Name','class':'form-control'}))
    email=forms.CharField(label='Enter User Name',widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email','class':'form-control '}))
    msg=forms.CharField(label='Enter User Name',widget=forms.Textarea(attrs={'placeholder':'Write Down Your Message','class':'form-control'}))
    class Meta:
        model = Contact
        fields = ("name","email","msg",)
        
class MyUserChangeFrm(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Enter your first name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }))
    last_name = forms.CharField(label='Enter your last name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }))
    email = forms.CharField(label='Enter your email*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }))
    contact_no = forms.CharField(label='Enter your contact number*', widget=forms.NumberInput(
        attrs={
            'class': 'form-control ',
        }))
    class Meta:
        model=CustomUser
        fields=['first_name', 'last_name', 'email', 'contact_no']
        
class MychangePwdForm(PasswordChangeForm):
    old_password = forms.CharField(label='Enter your current password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control ',
            
        }))
    new_password1 = forms.CharField(label='Enter your new password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control ',
             }))
    new_password2 = forms.CharField(label='Enter your confirm password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control ',
              }))
        
