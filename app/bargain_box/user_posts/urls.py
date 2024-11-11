from django.urls import path
from . import views

urlpatterns = [
    path('my-listings/', views.view_posts, name='view-posts'),
]
