from django.shortcuts import render
from django.http import HttpResponse

############################################ added (needed for sign out page to work correctly)
from django.contrib.auth import logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# Create your views here.
def user_account_registration(request):
    context = {
        'page_title': 'Register'
    }
    return render(request, 'user_authentication/register.html', context)


def user_account_signin(request):
    context = {
        'page_title': 'Sign in'
    }
    return render(request, 'user_authentication/signin.html', context)


#def user_account_signout(request):
#    context = {
#        'page_title': 'Signout'
#    }
#    return render(request, 'user_authentication/signout.html', context)


########################################### added (needed for sign out page to work correctly)
def user_account_signout(request):
    logout(request)
    return render(request, 'user_authentication/signout.html')


# Reset password
class PasswordResetView(PasswordResetView):
    template_name = "user_authentication/password_reset.html"

class PasswordResetEmailSentView(PasswordResetDoneView):
    template_name = "user_authentication/password_reset_email_sent.html"

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "user_authentication/password_reset_confirm.html"

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "user_authentication/password_reset_complete.html"