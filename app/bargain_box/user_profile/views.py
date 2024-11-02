from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Profile
from django.urls import reverse


# Create your views here.
@login_required
def view_profile(request):
    context = {
        'page_title': 'My profile',
    }

    return render(request, 'user_profile/view_profile.html', context)

def edit_profile(request):
    context = {
        'page_title': 'Edit my profile'
    }
    return render(request, 'user_profile/edit_profile.html', context)
