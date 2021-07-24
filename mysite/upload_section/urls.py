from django.urls import path

from . import views

app_name="upload_section"
urlpatterns = [
    path('', views.index, name='index'),
    path('submitted_post', views.submitted_post,name='submitted_post')
]