from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelFrom):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['usename','email','password']


