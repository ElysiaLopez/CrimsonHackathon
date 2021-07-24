from django import forms
from django.db.models.base import Model
from django.forms.widgets import Textarea
from .models import ImagePost, TextPost
from django.forms import ModelForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['post_title', 'pub_date', 'image_data']

# class UploadTextForm(forms.ModelForm):
#     text_data = forms.CharField(label='Text Post', max_length=100)

class TextUploadForm(ModelForm):
    class Meta:
        model = ImagePost
        #fields = ['post_title', 'pub_date', 'text_data']
        fields = '__all__'
        widgets = {
            'text_data': Textarea(attrs={'cols': 80, 'rows': 20})
        }