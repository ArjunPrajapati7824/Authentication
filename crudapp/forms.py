from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *


class studentform(UserCreationForm):
    password2 = forms.CharField(label='confirm password(again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}


class datachange(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
