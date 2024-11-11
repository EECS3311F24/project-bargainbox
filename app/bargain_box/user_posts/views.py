from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post

@login_required
def view_posts(request):
    user_posts = Post.objects.filter(author=request.user)

    return render(request, 'user_posts/view_posts.html', {'title': 'My listings', 'user_posts': user_posts})
