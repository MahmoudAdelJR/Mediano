from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class dive(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-3','placeholder':'Your name'}),label='')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg mb-3','placeholder':'Your Email'}),label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg mb-3','placeholder':'Password'}),label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg mb-4','placeholder':'Repeat your password'}),label='')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserLoginForm(AuthenticationForm):
  #  def __init__(self, *args, **kwargs):
   #     super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg mb-3', 'placeholder': 'Your Name ',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg mb-3',
            'placeholder': 'Your password',
        }
))
    class Meta:
            model = User
            fields = ['username','password']