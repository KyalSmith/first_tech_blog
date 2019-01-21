# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from blog_content.models import *
from .serializer import *



# Create your views here.


class Tutorial_Post_RUD_view(generics.RetrieveUpdateDestroyAPIView):


    lookup_field = 'pk'
    serializer_class = Tutorial_Serializer

    def get_queryset(self):
        return Tutorial.objects.all()


class Tutorial_Get_All_Posts(APIView):

    def get(self, request, format=None):
        tuts = Tutorial.objects.all()
        serializer = Tutorial_Serializer(tuts, many=True)
        return Response(serializer.data)




class Tutorial_Post_List_Create_view(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = Tutorial_Serializer


class Article_Post_RUD_view(generics.RetrieveUpdateDestroyAPIView):


    lookup_field = 'pk'
    serializer_class = Article_Serializer

    def get_queryset(self):
        return NewsArticle.objects.all()


class Article_Post_List_Create_view(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = Article_Serializer


class Article_Get_All_Posts(APIView):

    def get(self, request, format=None):
        articles = NewsArticle.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return Response(serializer.data)
