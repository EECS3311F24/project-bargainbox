from django.urls import path
from . import views

urlpatterns = [
    path('meet_the_team/', views.meet_the_team, name='meet_the_team'),
    path('how_we_work/', views.how_we_work, name='how_we_work' ),
]