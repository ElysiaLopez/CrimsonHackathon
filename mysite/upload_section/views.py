from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import UserPost, TextPost, ImagePost, FilePost

# Create your views here.

def index(request):
    posts_list = UserPost.objects.order_by('-pub_date')
    context = {'posts_list': posts_list}
    return render(request, 'upload_section/index.html', context)

def displayPosts():
    context = []
    