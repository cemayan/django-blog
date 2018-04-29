from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  class Meta:
    model = Post
    fields = (
      'id','data','created_date','user'
    )