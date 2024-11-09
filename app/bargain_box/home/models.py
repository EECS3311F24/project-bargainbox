
# imports
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

# attributes for Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True) # Allows pictures to be added to posts (pictures are optional)

    def __str__(self):
        return self.title

    # So that user is redirected to homepage once post is created
    def get_absolute_url(self):
        return reverse('home')