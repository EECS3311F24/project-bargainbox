from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Profile

# Create your views here.
def view_profile(request):
    # Check to make sure user is logged in
    if request.user.is_authenticated:
        context = {
            'page_title': 'My profile',
        }

        return render(request, 'user_profile/view_profile.html', context)
    else:
        # Not logged in so redirect to home page
        return HttpResponseRedirect(reverse('home'))

    

def edit_profile(request):
    context = {
        'page_title': 'Edit my profile'
    }
    return render(request, 'user_profile/edit_profile.html', context)
