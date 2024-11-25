from django.urls import path
from . import views

urlpatterns = [
    # The following route does not require the requesting client to be signed in.
    # The following route is used to view a seller's profile.
    path('view/<int:user_to_view_pk>/', views.view_profile, name = 'view-profile-given-user-pk'),

    # The following routes require the requesting client to be signed in.
    # The following routes are used to view, edit, and delete the signed in user's profile.
    path('view/', views.view_my_profile, name = 'view-profile'),
    path('edit/', views.edit_my_profile, name = 'edit-profile'),
    path('delete/', views.delete_my_profile, name = 'delete-profile')
]
