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
import redis,json
from django.http import JsonResponse
#from django.core.cache import cache

VERSIONS = (1,)
REDIS_DB = 2
MAX_ACTIVITIES = 10

r = redis.StrictRedis(host='localhost', port=6379, db=REDIS_DB,charset="utf-8", decode_responses=True)

#TODO: Tüm metodların hata yakalama kontrolleri yapılacak
class PostList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):  

        posts =Post.objects.all()     
        serializer = PostSerializer(posts,many=True)
        cache_data = r.hgetall("POSTS")
        if  cache_data :
            cache_data_last = r.hgetall("POSTS")      
            return Response(cache_data_last.values())
        else :
            if posts :
                for obj in json.loads(json.dumps(serializer.data)):
                    r.hset("POSTS",obj["id"],json.dumps(obj))     
                return Response(json.dumps(serializer.data))
            else :    
                return Response("")

    def post(self, request, format=None):   
        serializer = PostSerializer(data=request.data,context={'user_id': request.user.id})
        if serializer.is_valid():
            serializer_2 = PostSerializer(serializer.save())
            r.hset("POSTS",serializer_2.data["id"],json.dumps(serializer_2.data))
            return Response(json.dumps(serializer.data), status=status.HTTP_201_CREATED)
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
        data = json.loads(json.dumps(serializer.data))

        serializer_all = PostSerializer(Post.objects.all(),many=True)
        all_data = json.loads(json.dumps(serializer_all.data))
     
        key = "POSTS" 
        cache_data = eval(r.hget(key,pk))

        if(data["id"] == cache_data["id"]):
            print("cache")
            return Response(cache_data)
        else :  
            print("cache değil")     
            r.hset(key,data["id"],data)
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
          r.hdel("POSTS",pk)
          post_obj.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)