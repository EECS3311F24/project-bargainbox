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

urlpatterns = [
    path('', home_views.home_page, name = 'home'),
    path('register/', user_views.register, name='register'),
    path('register/', user_authentication_views.user_account_registration, name = 'register'),
    path('signin/', user_authentication_views.user_account_signin, name = 'signin'),
    path('signout/', user_authentication_views.user_account_signout, name = 'signout'),
    path('my-profile/', include('user_profile.urls')),
    path('admin/', admin.site.urls, name = 'admin')
]
