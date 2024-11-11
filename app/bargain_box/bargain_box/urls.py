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
from user_registration import views as user_registration_views

from django.contrib.auth import views as auth_views

from django.conf import settings   # added for pictures
from django.conf.urls.static import static # added for pictures
from post.views import PostListView # Displaying all posts in home

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'), # Displaying all posts in home

    path('post/', include("post.urls")),
    
    path('register/', user_registration_views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name = 'user_authentication/signin.html'), name = 'signin'),
    path("signout/", user_authentication_views.user_account_signout, name = 'signout'),
   
    path('my-profile/', include('user_profile.urls')),
    path('my-posts/', include('user_posts.urls')),
    path('admin/', admin.site.urls, name = 'admin')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
