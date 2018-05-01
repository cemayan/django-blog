from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from blog.models import Post,Profile
from rest_framework.fields import CurrentUserDefault

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 



class PostSerializer(serializers.ModelSerializer):
  #user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  user = UserSerializer(many=False,read_only=True)
  class Meta:
    model = Post
    fields = (
      'id','data','created_date','user'
    )
  def save(self):
    post = Post(
      data = self.validated_data["data"],
      user = Profile.objects.get(user_id = self.context.get("user_id"))
    )
    post.save()
    return post

