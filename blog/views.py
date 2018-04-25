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


# @api_view(['GET'])  
# def all_post(request):
#     products = Post.objects.all()
#     return Response(products, status=status.HTTP_201_CREATED)


# @api_view(['POST'])  
# def new_post(request):
#    if request.method == 'POST':
#       return Response({"message": "Got some data!", "data": request.data})
#    return Response({"message": "Hello, world!"})

