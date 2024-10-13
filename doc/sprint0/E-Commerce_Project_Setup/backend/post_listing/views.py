from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Post_listing_Serializer
from .models import Post_listing

# Create your views here.

class Post_listing_View(viewsets.ModelViewSet):
    serializer_class = Post_listing_Serializer
    queryset = Post_listing.objects.all()