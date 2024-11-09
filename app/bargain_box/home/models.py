
# imports
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Note: Each class will be its own table in the database

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title