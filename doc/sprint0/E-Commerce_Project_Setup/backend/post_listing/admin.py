from django.contrib import admin
from .models import Post_listing

class post_listing_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Post_listing, post_listing_admin)