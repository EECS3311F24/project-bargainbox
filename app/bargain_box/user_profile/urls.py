from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_profile, name = 'view-profile'), # used to view the signed in user's profile
    path('view/<int:pk>/', views.view_profile, name = 'post-detail-given-user-pk'), # used to view a non-signed in user's profile
    path('edit/', views.edit_profile, name = 'edit-profile'),
    path('delete/', views.delete_profile, name = 'delete-profile')
]
