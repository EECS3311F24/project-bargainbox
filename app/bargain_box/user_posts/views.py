from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_posts(request):
    return render(request, 'user_posts/view_posts.html', {'title': 'My listings'})
