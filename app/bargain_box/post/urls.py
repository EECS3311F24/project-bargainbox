from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
    path('post_edit/<int:pk>/', PostUpdateView.as_view(), name = 'post-edit') # added for edit view
]