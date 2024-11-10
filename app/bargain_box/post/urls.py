from django.urls import path

from .views import PostDetailView, PostCreateView, PostEditView

urlpatterns = [
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('new/', PostCreateView.as_view(), name = 'post-create'), # added for post creation view
    #########
    # Since there is mismatch in the model so I didn't configure for you right away Annie
    # but feel free to delete these comemnts and make your own url, Timothy 
    #
    # path('edit/<int:pk>/', PostEditView.as_view(), name = 'post-edit'), # added for edit view
    #########
]