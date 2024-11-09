from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserProfileForm

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


@login_required
def edit_profile(request):
    context = {
        'page_title': 'Edit profile',
        'form': None
    }

    if request.method == 'GET':
        profile_update_form = UpdateUserProfileForm(instance=request.user)
        context['form'] = profile_update_form

        return render(request, 'user_profile/edit_profile.html', context)
    
    elif request.method == 'POST':
        profile_update_form = UpdateUserProfileForm(request.POST, instance=request.user)

        if profile_update_form.is_valid():
            profile_update_form.save()
            messages.success(request, 'Your account profile has been successfully updated.')
            return redirect('view-profile')
        else:
            context['form'] = profile_update_form

            return render(request, 'user_profile/edit_profile.html', context)
