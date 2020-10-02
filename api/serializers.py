from django.db.models import fields
from rest_framework import serializers
from api.models import  Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['up_votes', 'down_votes', 'post_date', 'content', 'id', 'post_type', 'vote_counter']

