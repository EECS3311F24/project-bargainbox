from django.shortcuts import render
from django.http import HttpResponse


# import added
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', context)

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
    fields = ['title', 'content', 'location', 'quantity', 'price']

    # sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)