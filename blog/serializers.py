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
  def get_post(self):
    post = Post(
      data = Post.objects.get(id = self.context.get("id")),
      user = Profile.objects.get(user_id = self.context.get("user_id"))
    )
    return post

  def save(self):
    post = Post(
      data = self.validated_data["data"],
      user = Profile.objects.get(user_id = self.context.get("user_id"))
    )
    if self.context.get("method")=='PUT':
        _post = Post.objects.filter(id = self.context.get("id")).update(data=self.validated_data["data"])
        post = Post(
          id = self.context.get("id"),
          data = self.validated_data["data"],
          user = Profile.objects.get(user_id = self.context.get("user_id"))
        )
        return post
        
    else :  
      post.save()
      return post

