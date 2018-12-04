# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Topic(models.Model):
    tech_type = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.tech_type

class Tutorial(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(unique=True,max_length=256,default="")
    category = models.ForeignKey(Topic,on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)
    date_modified = models.DateField(null=True,blank=True)
    description = models.TextField()
    Content = models.TextField()
    search_criteria = models.TextField()
    content_html = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog_content:list_news')

    def __str__(self):
        return self.Title


class TutLikeCount(models.Model):
    tut = models.OneToOneField(Tutorial,unique=True,on_delete=models.CASCADE)
    users = models.TextField(default="[]")


    def __str__(self):
        return str(self.tut)


class TutorialComment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Tutorial = models.ForeignKey(Tutorial,on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateField(default=timezone.now())

    def __str__(self):
        return self.comment






class NewsArticle(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(unique=True,max_length=256,default="")
    date_created = models.DateField(default=timezone.now)
    description = models.TextField()
    Content = models.TextField()
    search_criteria = models.TextField()
    content_html = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog_content:list_news')

    def __str__(self):
        return self.Title


class NewsLikeCount(models.Model):
    news = models.OneToOneField(NewsArticle,unique=True,on_delete=models.CASCADE)
    users = models.TextField(default="[]")


    def __str__(self):
        return str(self.news)



class NewsComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_article = models.ForeignKey(NewsArticle)
    comment = models.TextField()
    date_commented = models.DateField(default=timezone.now())







