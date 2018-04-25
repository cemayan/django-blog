from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from account.forms import LoginForm,RegisterForm
from blog.models import Profile
from django.http import HttpResponse

def login_view(request):
  form = LoginForm(request.POST or None)
  if request.method == 'POST' : 

      if form.is_valid():
          username = form.cleaned_data.get('username')
          password= form.cleaned_data.get('password')
          user = authenticate(username=username,password=password)
          login(request,user)
          return redirect('home')
  return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')



def register_view(request):
  if request.method =='POST' :
      form = RegisterForm(request.POST or None)
      if form.is_valid():

        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        firstname = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')

        user.set_password(password)
        user.save()

        profile = Profile()
        profile.user = User.objects.get(id=user.id)
        profile.save()
        return render(request,'accounts/register.html')
  return render(request,'accounts/register.html')   