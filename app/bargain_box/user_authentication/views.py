from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_account_registration(request):
    context = {
        'page_title': 'Create an account'
    }
    return render(request, 'user_authentication/register.html', context)

def user_account_signin(request):
    context = {
        'page_title': 'Signin'
    }
    return render(request, 'user_authentication/signin.html', context)

def user_account_signout(request):
    context = {
        'page_title': 'Signout'
    }
    return render(request, 'user_authentication/signout.html', context)
