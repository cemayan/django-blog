from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from blog.models import Post,Profile,Comment
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      'username','id'
    )


class ProfileSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False,read_only=True)
  class Meta:
        model = Profile
        #fields = '__all__' 
        fields= (
          'user','image'
        )


class PostSerializer(serializers.ModelSerializer):
  #user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  user = ProfileSerializer(many=False,read_only=True)
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

class PostSerializer2(serializers.ModelSerializer):
    class Meta:
      model = Post
      fields = (
        'id',
      )


class CommentSerializer(serializers.ModelSerializer):
  #post= PostSerializer(many=False)
  user = ProfileSerializer(many=False,read_only=True)
  class Meta: 
    model = Comment
    fields  =('id','created_date','post','data','user'
    )
  def save(self):

    comment = Comment(
      data = self.validated_data["data"],
      user = Profile.objects.get(user_id = self.context.get("user_id")),
      post = Post.objects.get(id = self.data["post"])
    )
    comment.save()
    return comment