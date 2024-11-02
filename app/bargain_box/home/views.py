from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'home/home.html', context)
