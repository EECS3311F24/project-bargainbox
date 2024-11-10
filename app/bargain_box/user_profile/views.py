from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.models import User

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

@login_required
def delete_profile(request):
    if request.method == 'GET':
        return render(request, 'user_profile/delete_profile.html', {'page_title': 'Delete profile'})
    
    elif request.method == 'DELETE':
        #record the primary key of the currently signed in user
        deleted_user_primary_key = request.user.pk
        #sign the user out
        logout(request)
        #delete the user from the User table in the database
        User.objects.get(pk=deleted_user_primary_key).delete()

        return HttpResponse(content='true', content_type="application/json; charset=utf-8", status=200, reason="OK", charset="utf-8")
