from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserTableForm, UpdateProfileTableForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from user_profile.models import Profile
from post.models import Post

def view_profile(request, user_to_view_pk):
    if request.method == 'GET':
        context = {
            'page_title': 'User profile',
            'origin_URL': None,
            'user_to_view': None,
            'allow_edit_and_delete': False,
            'user_active_listings': 0
        }

        '''
        When the user is viewing a listing, they have the option to click on the seller's name to view view their profile.
        When the user arrives on a seller's profile page, it would nice to have a back button so that the user can easily
        get back to the listing they were previously viewing. Here, this is implemented using a URL query string.
        The 'origin' key in the URL query string specifies where the user should be taken back to upon clicking the back button.
        If there is no URL query string, or the 'origin' key is absent from the URL query string, do not display the back button.

        Resources used:
        https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.HttpRequest.GET
        https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.QueryDict.__getitem__
        '''

        try:
            context['origin_URL'] = request.GET.__getitem__('origin')
        except KeyError:
            pass

        # Get all User objects with a primary key that matches the primary key encoded in the request's URL.
        user_to_view = User.objects.filter(pk=user_to_view_pk)

        # If the number of User objects with a matching primary key is not equal to 1, the request is invalid, so return a HTTP 400 response.
        if user_to_view.count() != 1:
            return HttpResponse(content='400 Bad Request', content_type="text/plain; charset=utf-8", status=400, reason="Bad Request", charset="utf-8")
        else:
            user_to_view = user_to_view.first()
            context['user_to_view'] = user_to_view

        # Get the number of Post objects that belong to the target User.
        user_active_listings = Post.objects.filter(author=user_to_view.pk).count()
            
        # If the user has 0 associated Post objects, there is no reason for their profile to be publically accessible by other users.
        if user_active_listings == 0:
            return HttpResponse(content='401 Unauthorized', content_type="text/plain; charset=utf-8", status=401, reason="Unauthorized", charset="utf-8")
        else:
            context['user_active_listings'] = user_active_listings
        
        return render(request, 'user_profile/view_profile.html', context)

    else:
        # If the HTTP request method is not GET, return a HTTP 405 response.
        return HttpResponse(content='405 Method Not Allowed', content_type="text/plain; charset=utf-8", status=405, reason="Method Not Allowed", charset="utf-8")

@login_required
def view_my_profile(request):
    if request.method == 'GET':
        context = {
            'page_title': 'My profile',
            'origin_URL': None,
            'user_to_view': request.user,
            'allow_edit_and_delete': True,
            'user_active_listings': Post.objects.filter(author=request.user.pk).count()
        }
        return render(request, 'user_profile/view_profile.html', context)

    else:
        # If the HTTP request method is not GET, return a HTTP 405 response.
        return HttpResponse(content='405 Method Not Allowed', content_type="text/plain; charset=utf-8", status=405, reason="Method Not Allowed", charset="utf-8")
    

@login_required
def edit_my_profile(request):
    context = {
        'page_title': 'Edit profile',
        'username_and_email_form': None,
        'image_and_biography_form': None
    }

    if request.method == 'GET':
        update_user_form = UpdateUserTableForm(instance=request.user)

        '''
        Instead of directly passing the user's Profile record from the database to the form,
        a temporary copy of the user's Profile record is created then passed instead. This is to
        prevent the frontend application from displaying the current profile picture's file name.
        Doing it this way makes things prettier and less confusing for the end user.
        '''
        temp_profile_instance = Profile(
            id = request.user.profile.id,
            user_id = request.user.profile.user_id,
            image = None,
            biography = request.user.profile.biography
        )

        update_profile_form = UpdateProfileTableForm(instance=temp_profile_instance)
        context['username_and_email_form'] = update_user_form
        context['image_and_biography_form'] = update_profile_form

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
            context['image_and_biography_form'] = UpdateProfileTableForm()
            
            return render(request, 'user_profile/edit_profile.html', context)

    else:
        # If the HTTP request method is not GET or POST, return a HTTP 405 response.
        return HttpResponse(content='405 Method Not Allowed', content_type="text/plain; charset=utf-8", status=405, reason="Method Not Allowed", charset="utf-8")

@login_required
def delete_my_profile(request):
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

    else:
        # If the HTTP request method is not GET or DELETE, return a HTTP 405 response.
        return HttpResponse(content='405 Method Not Allowed', content_type="text/plain; charset=utf-8", status=405, reason="Method Not Allowed", charset="utf-8")
