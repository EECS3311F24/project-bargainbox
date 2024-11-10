from django.shortcuts import render

# Create your views here.
# import added
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# this is our class based view for listing all posts
class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# this is our class based view for detailed view of an individual post
class PostDetailView(DetailView):
    model = Post

# this is our class based view for creating a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'location', 'quantity', 'price', 'image']

    # sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)