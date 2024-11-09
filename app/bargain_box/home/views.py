from django.shortcuts import render
from django.http import HttpResponse

# import added
from .models import Post

# Create your views here.
def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', context)
