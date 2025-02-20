from django.shortcuts import render

# Create your views here.
# import added
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

#imports added for bookmarks
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import View

from django.urls import reverse_lazy

# classes created for the add bookmark view
class AddingBookmarkView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        bookmark = get_object_or_404(Post, id = post_id)
        bookmark.bookmarks.add(request.user)
        return redirect('home')

# class based view created for listing all bookmarked posts by a user
class BookmarkView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/bookmarked_posts.html'
    context_object_name = 'bookmarked_posts'

    # this function is used to get all of the posts that the user has bookmarked
    def get_queryset(self):
        queryset = Post.objects.filter(bookmarks = self.request.user)
        return queryset


# created for remove bookmark view for Timothy when you are working on this part
class RemovingBookmarkView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        bookmark = get_object_or_404(Post, id=post_id)
        bookmark.delete()
        return redirect(reverse_lazy('home')) # Delete first before redirecting

# this is our class based view for listing all posts
class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('query', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(location__icontains=search_query)
            )
        return queryset        

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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post/post_edit.html"
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

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template = "post/post_confirm_delete.html"
    success_url = '/'  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #checks if the current user is the author of the post!
            return True
        return False 