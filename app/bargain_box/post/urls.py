from django.urls import path

from .views import PostDetailView, PostCreateView

urlpatterns = [
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
]