from django.shortcuts import render
from .serializers import PostListSerializer
from rest_framework import generics
from blog.models import Post as PostLists
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = PostLists.objects.all().order_by('-created_on')
    serializer_class = PostListSerializer

class PostOne(APIView):
    def get(self, request, slug):
        post = PostLists.objects.filter(slug = slug)
        serializer = PostListSerializer(post, many=True)
        return Response({"post": serializer.data})

class PostsUser(APIView):
    def get(self, request, user):
        posts = PostLists.objects.filter(user = user)
        serializer = PostListSerializer(posts, many=True)
        return Response({"posts": serializer.data})

class PostUser(APIView):
    def get(self, request, slug,user):
        post = PostLists.objects.filter(slug = slug).order_by('-created_on')
        serializer = PostListSerializer(post, many=True)
        return Response({"post": serializer.data})
    def delete(self, request, slug,user):
        article = get_object_or_404(PostLists.objects.all(), slug=slug)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(slug)
        }, status=204)
