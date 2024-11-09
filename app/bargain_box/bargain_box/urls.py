"""
URL configuration for bargain_box project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from home import views as home_views
from user_authentication import views as user_authentication_views
from users import views as user_views

from django.contrib.auth import views as auth_views

from home.views import PostListView, PostDetailView, PostCreateView # updated

urlpatterns = [
    path('', home_views.PostListView.as_view(), name = 'home'), # updated
    path('post/<int:pk>/', home_views.PostDetailView.as_view(), name = 'post-detail'), # added for detailed view
    path('post/new/', home_views.PostCreateView.as_view(), name = 'post-create'), # added for post creation view

    path('register/', user_views.register, name='register'),
    path('register/', user_authentication_views.user_account_registration, name = 'register'),

    path('signin/', auth_views.LoginView.as_view(template_name = 'user_authentication/signin.html'), name = 'signin'),
    path("signout/", user_authentication_views.user_account_signout, name = 'signout'),
   
    path('my-profile/', include('user_profile.urls')),
    path('admin/', admin.site.urls, name = 'admin')
]
