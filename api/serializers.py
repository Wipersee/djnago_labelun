from rest_framework import serializers
from blog.models import Post,Comment,Category, Profile
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ['author', 'body', 'created_on','post']

class PostListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    #categories = CategorySerializer(many=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title','body','created_on','categories','slug','comments','user']

    

