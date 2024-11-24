from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# added for view, add, and remove bookmarks
from .views import AddingBookmarkView
from .views import RemovingBookmarkView
from .views import BookmarkView

urlpatterns = [
    # paths added for view, add, and remove bookmarks
    path('<int:post_id>/add-bookmark/', AddingBookmarkView.as_view(), name = 'adding_bookmark'),
    path('<int:post_id>/remove-bookmark/', RemovingBookmarkView.as_view(), name = 'removing_bookmark'),
    path('bookmarks/', BookmarkView.as_view(), name = 'bookmarked_posts'),
    

    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
    path('view/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('edit/<int:pk>/', PostUpdateView.as_view(), name = 'post-edit'), # added for edit view
    path('delete/<int:pk>/', PostDeleteView.as_view(), name = 'post-delete'), # added for edit view
]