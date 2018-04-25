from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  


class Post(models.Model):
  title = models.CharField(max_length=120)
  content = JSONField()
  created_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile,to_field='user',null=True,on_delete=None)

