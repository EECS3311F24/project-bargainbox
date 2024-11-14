from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
    path('post_edit/<int:pk>/', PostUpdateView.as_view(), name = 'post-edit'), # added for edit view
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name = 'post-delete'), # added for edit view

]