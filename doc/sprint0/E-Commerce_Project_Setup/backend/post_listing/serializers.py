from rest_framework import serializers
from .models import Post_listing

class Post_listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post_listing
        fields = ('id', 'title', 'description', 'completed')