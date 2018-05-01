from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post
from django.contrib.auth.decorators import login_required

def home_view(request):
  if request.user.is_authenticated: 
    return render(request,'home/index.html')
  else :
    return HttpResponseRedirect('/login')

def post_detail(request,id):
  if request.user.is_authenticated: 
    return render(request,'posts/detail.html')
  else :
    return HttpResponseRedirect('/login')