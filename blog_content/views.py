# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
import unicodedata



# Create your views here.

class home(TemplateView):
    template_name = "blog_content/home.html"


class List_Python(ListView):
    model = Tutorial
    template_name = "blog_content/List_Python.html"

    def get_queryset(self):
        topic_val = Topic.objects.get(tech_type='Python')
        queryset = Tutorial.objects.filter(category=topic_val.id)
        return queryset



class List_Linux(ListView):
    model = Tutorial
    template_name = "blog_content/List_Linux.html"

    def get_queryset(self):
        topic_val = Topic.objects.get(tech_type='Linux')
        queryset = Tutorial.objects.filter(category=topic_val.id)
        return queryset

class List_Bash(ListView):
    model = Tutorial
    template_name = "blog_content/List_Bash.html"

    def get_queryset(self):
        topic_val = Topic.objects.get(tech_type='Bash')
        queryset = Tutorial.objects.filter(category=topic_val.id)
        return queryset


class List_Perl(ListView):
    model = Tutorial
    template_name = "blog_content/List_Perl.html"

    def get_queryset(self):
        topic_val = Topic.objects.get(tech_type='Perl')
        queryset = Tutorial.objects.filter(category=topic_val.id)
        return queryset

class List_News(ListView):
    model = NewsArticle
    template_name = "blog_content/List_Articles.html"

class News_Detail(DetailView):
    model = NewsArticle
    template_name = "blog_content/News_Detail.html"

    def get_context_data(self,**kwargs):

        context = super(News_Detail,self).get_context_data(**kwargs)
        context['comments'] = NewsComment.objects.filter(news_article = kwargs['object'])
        try:
            like_list = str(NewsLikeCount.objects.get(news=kwargs['object']).users).split(',')
            del like_list[len(like_list)-1]
        except:
            like_list = []

        context['likes'] = len(like_list)



        if self.request.user.username in like_list:
            context['already_liked'] = True
            print("User is in like list")

        else:
            context['alread_liked'] = False
            print("User is not in like list")

        return context

def News_Comment_Update(request):

    if request.method=="POST" and request.is_ajax():
        try:
            user_ob = request.user
            title = request.POST['title']
            title_ob = NewsArticle.objects.get(Title=title)
            this_comment = request.POST['comment']
            write = NewsComment(author=user_ob,news_article=title_ob,comment=this_comment)
            write.save()
            print("saved!")
            return JsonResponse({'status':'Success','msg':'saved comment successfully'})
        except TutorialComment.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})





class Tut_Detail(DetailView):
    model = Tutorial
    template_name = "blog_content/Tut_Detail.html"

    def get_context_data(self,**kwargs):

        context = super(Tut_Detail,self).get_context_data(**kwargs)
        context['comments'] = TutorialComment.objects.filter(Tutorial = kwargs['object'])
        try:
            like_list = str(TutLikeCount.objects.get(tut=kwargs['object']).users).split(',')
            del like_list[len(like_list)-1]

        except Exception as e:

            print (e)
            like_list = []

        print(len(like_list))
        context['likes'] = len(like_list)



        if self.request.user.username in like_list:
            context['already_liked'] = True
            print("User is in like list")

        else:
            context['alread_liked'] = False
            print("User is not in like list")

        return context


def Tut_Comment_Update(request):

    if request.method=="POST" and request.is_ajax():
        try:
            user_ob = request.user
            title = request.POST['title']
            title_ob = Tutorial.objects.get(Title=title)
            this_comment = request.POST['comment']
            write = TutorialComment(author=user_ob,Tutorial=title_ob,comment=this_comment)
            write.save()
            print("saved!")
            return JsonResponse({'status':'Success','msg':'saved comment successfully'})
        except TutorialComment.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


class add_tutorial(CreateView):
    model = Tutorial
    fields = ['Title', 'category', 'description', 'Content', 'search_criteria', 'content_html']
    template_name = "blog_content/add_tutorial.html"

    def form_valid(self,form):
        user = self.request.user
        form.instance.author = user

        return super(add_tutorial,self).form_valid(form)


class add_article(CreateView):
    model = NewsArticle
    fields = ['Title', 'description', 'Content', 'search_criteria', 'content_html']
    template_name = "blog_content/add_article.html"


    def form_valid(self,form):
        user = self.request.user
        form.instance.author = user

        return super(add_article,self).form_valid(form)



def add_news_like(request):

    if request.method == "POST" and request.is_ajax():

        try:
            title = request.POST['title']
            user = request.user
            news_obj = NewsArticle.objects.get(Title=title)

            if not NewsLikeCount.objects.filter(news=news_obj).exists():

                news_like_obj = NewsLikeCount(news = news_obj,users = str(request.user)+",")

            else:

                news_like_obj = NewsLikeCount.objects.get(news=news_obj)

                user_list = str(news_like_obj.users)
                if request.user.username not in user_list:
                    user_list+=str(request.user)+","
                    news_like_obj.users = str(user_list)

            news_like_obj.save()

            return JsonResponse({'status': 'Success', 'msg': 'like saved successfully'})

        except NewsArticle.DoesNotExist:

            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})




def add_tut_like(request):
    if request.method == "POST" and request.is_ajax():

        try:
            title = request.POST['title']

            tut_obj = Tutorial.objects.get(Title=title)
            if not TutLikeCount.objects.filter(tut=tut_obj).exists():
                tut_like_obj = TutLikeCount(tut=tut_obj, users= str(request.user) + ",")
            else:
                tut_like_obj = TutLikeCount.objects.get(tut=tut_obj)
                user_list = str(tut_like_obj.users)
                if request.user.username not in user_list:
                    user_list += str(request.user) + ","
                    tut_like_obj.users = str(user_list)

            tut_like_obj.save()

            return JsonResponse({'status': 'Success', 'msg': 'like saved successfully'})

        except Tutorial.DoesNotExist:

            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})



def search_item(request):
    if request.method=="POST":
        news_criteria = {}
        tut_criteria = {}
        news_articles = NewsArticle.objects.all()
        tuts = Tutorial.objects.all()
        for article in news_articles:
            data = article.search_criteria.lower()
            if ',' in data:
                delimitied_data = data.split(',')
                news_criteria[article.Title] = delimitied_data
            else:
                news_criteria[article.Title] = data

        for tut in tuts:
            tut_data = tut.search_criteria.lower()
            if ',' in tut_data:
                tut_delimitied_data = tut_data.split(',')
                tut_criteria[tut.Title] = tut_delimitied_data
            else:
                tut_criteria[tut.Title] = tut_data

        print(news_criteria)
        print(tut_criteria)

        form_data = request.POST.get('search_criteria').lower()
        matching_news_items = []
        matching_tut_items = []

        for entry in news_criteria:

            if isinstance(news_criteria[entry],list):
                for item in news_criteria[entry]:
                    if form_data in item:
                        matching_news_items.append(NewsArticle.objects.get(Title=entry))
                        break


            else:
                if form_data in news_criteria[entry]:
                    matching_news_items.append(NewsArticle.objects.get(Title=entry))


        for entry in tut_criteria:

            if isinstance(tut_criteria[entry],list):
                for item in tut_criteria[entry]:
                    if form_data in item:
                        matching_tut_items.append(Tutorial.objects.get(Title=entry))
                        break


            else:
                if form_data in tut_criteria[entry]:
                    matching_tut_items.append(Tutorial.objects.get(Title=entry))

        return render(request,"blog_content/results.html",{"news":matching_news_items,"tuts":matching_tut_items})
    return render(request,"blog_content/results.html")



class Update_News(UpdateView):
    model = NewsArticle
    fields = ['Title', 'description', 'Content', 'search_criteria', 'content_html']
    template_name = "blog_content/update_news.html"

class Update_Tut(UpdateView):
    model = Tutorial
    fields = ['Title', 'category', 'description', 'Content', 'search_criteria', 'content_html']
    template_name = 'blog_content/update_tut.html'

def List_User_Articles(request):

    user_articles = NewsArticle.objects.filter(author=request.user)
    user_tuts = Tutorial.objects.filter(author=request.user)

    return render(request,"blog_content/user_blogs.html",{"news":user_articles,"tuts":user_tuts})





#unicodedata.normalize('NFKD',article.search_criteria).encode('ascii','ignore').lower()





#unicodedata.normalize('NFKD', raw_text).encode('ascii','ignore')
