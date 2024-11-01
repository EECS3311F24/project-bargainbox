from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name = 'view-profile'),
    path('edit/', views.edit_profile, name = 'edit-profile')
]
