from django.urls import path
from . import views

urlpatterns = [
    path('meet_the_team/', views.meet_the_team, name='meet_the_team'),
]