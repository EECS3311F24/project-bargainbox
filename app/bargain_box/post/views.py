from django.shortcuts import render

# Create your views here.
# import added
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# this is our class based view for listing all posts
class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# this is our class based view for detailed view of an individual post
class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"


# this is our class based view for creating a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'location', 'quantity', 'price', 'image']

    # sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# this is our class based view for editting individual post
class PostEditView(UpdateView):
    model = Post
    template_name = "post/post_edit.html"

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'location', 'quantity', 'price', 'image']

    # sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #checks if the current user is the author of the post!
            return True
        return False 