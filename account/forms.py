from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# -*- coding: utf-8 -*-

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100,widget=forms.PasswordInput)
  def clean(self):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    if username and password :
       user = authenticate(username=username,password=password)
       if not user : 
          raise forms.ValidationError('Bulunamadi')
    return super(LoginForm,self).clean()  

class RegisterForm(forms.ModelForm):
  first_name  = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  email = forms.CharField(max_length=100)
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100,widget=forms.PasswordInput)
  def clean(self):
    
    first_name = self.cleaned_data.get('firstname')
    last_name = self.cleaned_data.get('lastname')
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

  class Meta: 
    model = User
    fields = [
      'username',
      'password',
      'email',
      'first_name',
      'last_name'
    ]
       

