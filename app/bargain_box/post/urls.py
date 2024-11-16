from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
    path('view/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('edit/<int:pk>/', PostUpdateView.as_view(), name = 'post-edit'), # added for edit view
    path('delete/<int:pk>/', PostDeleteView.as_view(), name = 'post-delete'), # added for edit view
]