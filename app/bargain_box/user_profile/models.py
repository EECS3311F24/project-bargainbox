from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='profile_images/default.png')
    biography = models.TextField(max_length=1000, default='none')

    def __str__(self):
        return self.user.username
