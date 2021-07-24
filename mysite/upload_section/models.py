from django.db import models
from django.utils import timezone

max_text_length = 2000

class UploadArea(models.Model):
    text_field = models.TextField()
    def __str__(self):
        return "Upload Area"

#base class for all types of posts (e.g. text-based, picture, video)
class UserPost(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    #data = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.post_title

class TextPost(UserPost):
    text_data = models.TextField(max_length=max_text_length, default='')
    

class ImagePost(UserPost):
    image_data = models.ImageField(upload_to='images/', default='flower-in-desert.jpg')
    # image_data.upload_to = 'images/'
    # image_data.default = 'flower-in-desert.jpg'

class FilePost(UserPost):
    pass#file_data = models.FileField()
