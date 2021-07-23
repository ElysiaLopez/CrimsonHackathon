from django.contrib import admin
from .models import TextPost, ImagePost, FilePost

admin.site.register(ImagePost)
admin.site.register(TextPost)
admin.site.register(FilePost)
# Register your models here.
