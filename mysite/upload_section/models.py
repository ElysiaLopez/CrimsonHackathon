from django.db import models
from django.utils import timezone

max_text_length = 1000

class UploadArea(models.Model):
    text_field = models.CharField(max_length=max_text_length, blank = True)

    def __str__(self):
        return "Upload Area"

#base class for all types of posts (e.g. text-based, picture, video)
class UserPost(models.Model):
    post_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title

class TextPost(UserPost):
    text_data = models.CharField(max_length=max_text_length)
    

class ImagePost(UserPost):
    image_data = models.ImageField()

class FilePost(UserPost):
    file_data = models.FileField()
