from django.shortcuts import render

# Create your views here.
def view_posts(request):
    return render(request, 'user_posts/view_posts.html', {'title': 'My listings'})
