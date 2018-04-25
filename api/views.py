from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import  PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
import redis
#from django.core.cache import cache

VERSIONS = (1,)
REDIS_DB = 2
MAX_ACTIVITIES = 10

r = redis.StrictRedis(host='localhost', port=6379, db=REDIS_DB)

class PostList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)



  
    def get(self, request, format=None):  
        r.hmset("another_user", {'name': 'robert', 'age': 32})
        #cache.set("foo","value",timeout=2500)   
        #print(cache.get("foo"))
        posts =Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)  


    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetail(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    

    def get(self, request,pk, format=None):     
        posts =self.get_object(pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  
          post_obj = self.get_object(pk)
          serializer = PostSerializer(post_obj, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
          post_obj = self.get_object(pk)
          post_obj.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)