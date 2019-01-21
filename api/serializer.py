from rest_framework import serializers
from blog_content.models import *


class Tutorial_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Tutorial
        fields = '__all__'


class Article_Serializer(serializers.ModelSerializer):

    class Meta:
        model = NewsArticle
        fields = '__all__'
