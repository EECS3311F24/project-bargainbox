from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_profile, name = 'view-profile'),
    path('edit/', views.edit_profile, name = 'edit-profile'),
    path('delete/', views.delete_profile, name = 'delete-profile')
]
