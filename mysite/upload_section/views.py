from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import UploadArea, UserPost, TextPost, ImagePost, FilePost

from .forms import TextUploadForm

# Create your views here.

def index(request):
    text_posts_list = TextPost.objects.order_by('-pub_date')
    image_posts_list = ImagePost.objects.order_by('-pub_date')
    file_posts_list = FilePost.objects.order_by('-pub_date')
    context = {
        'text_posts_list': text_posts_list,
        'image_posts_list': image_posts_list,
        'file_posts_list':file_posts_list
    }
    return render(request, 'upload_section/index.html', context)

def submitted_post(request):
    if request.method == 'POST':
        form = TextUploadForm(request.POST)
        if form.is_valid():
            post_title = form.__getattribute__('post_title')
            pub_date = form.__getattribute__('pub_date')
            text_data = form.__getattribute__('text_data')
            return HttpResponseRedirect("Submitted!")   
    else:
        form = TextUploadForm()
    return render(request, 'upload_section/submitted_post.html')

def image_upload_test(request):
    return render(request, 'image_upload_test.html')

def post_text(request):
    # upload_area = UploadArea.objects.create(text_field="blah")
    # upload_area.save()
    # return render(request, '')

    #new_post = TextPost(post_title=title, pub_date=pub_date, text_data=text)
    pass

def post_image(image: ImagePost):
    pass

def post_file(file: FilePost):
    pass
