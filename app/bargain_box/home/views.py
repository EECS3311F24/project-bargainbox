from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from post.models import Post


def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', context)
