from django.shortcuts import render
from django.http import request
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Post
from api.serializers import PostSerializer

# Create your views here.
## Nikal helped me with this.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False)
    def Roast(self, request):
        roast = Post.objects.filter(post_type=False).order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def Total(self, request):
        roast = Post.objects.filter(post_type=False).order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Boast(self, request):
        boast = Post.objects.filter(post_type=True).order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def up_vote(self, request, pk=None):
 
        post = self.get_object()
        post.up_votes += 1
        post.save()
        return Response({'status': 'votedup'})

    @action(detail=True, methods=['get', 'post'])
    def down_vote(self, request, pk=None):
      
        post = self.get_object()
        post.down_votes += 1
        post.save()
        return Response({'status': 'voteddown'})
    
