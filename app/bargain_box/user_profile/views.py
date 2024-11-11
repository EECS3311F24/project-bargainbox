from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserTableForm, UpdateProfileTableForm
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
        'username_and_email_form': None,
        'image_form': None
    }

    if request.method == 'GET':
        update_user_form = UpdateUserTableForm(instance=request.user)
        update_profile_form = UpdateProfileTableForm()
        context['username_and_email_form'] = update_user_form
        context['image_form'] = update_profile_form

        return render(request, 'user_profile/edit_profile.html', context)
    
    elif request.method == 'POST':
        update_user_form = UpdateUserTableForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileTableForm(request.POST, request.FILES, instance=request.user.profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request, 'Your account profile has been successfully updated.')
            return redirect('view-profile')
        else:
            context['username_and_email_form'] = update_user_form
            context['image_form'] = update_profile_form

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
