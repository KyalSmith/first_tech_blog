from django.forms import ModelForm
from .models import *


class News_Form(ModelForm):

    class Meta:
        model = NewsArticle
        fields = ['Title','description','Content','search_criteria','content_html']


class Tutorial_Form(ModelForm):

    class Meta:
        model = Tutorial
        fields = ['Title','category','description','Content','search_criteria','content_html']