from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_profile(request):
    context = {
        'page_title': 'My profile'
    }
    return render(request, 'user_profile/view_profile.html', context)

def edit_profile(request):
    context = {
        'page_title': 'Edit my profile'
    }
    return render(request, 'user_profile/edit_profile.html', context)
