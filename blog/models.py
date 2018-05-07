from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.TextField(null=True)
  


class Post(models.Model):
  data = JSONField()
  created_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile,to_field='user',null=True,on_delete=None)

class Comment(models.Model): 
  data = JSONField(null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post,to_field='id',null=False,on_delete=None)
  user = models.ForeignKey(Profile,to_field='user',null=True,on_delete=None)