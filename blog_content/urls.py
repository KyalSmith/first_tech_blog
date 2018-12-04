"""tech_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name="blog_content"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$',home.as_view(),name="home"),
    url(r'list_linux$',List_Linux.as_view(),name="list_linux"),
    url(r'list_python$',List_Python.as_view(),name="list_python"),
    url(r'list_bash$',List_Bash.as_view(),name="list_bash"),
    url(r'list_perl$',List_Perl.as_view(),name="list_perl"),
    url(r'list_news$',List_News.as_view(),name="list_news"),
    url(r'^tut_detail/(?P<pk>[-\w]+)/$',Tut_Detail.as_view(),name="tut_detail"),
    url(r'^news_detail/(?P<pk>[-\w]+)/$',News_Detail.as_view(),name="news_detail"),
    url(r'^news_detail/',add_news_like,name="like_article"),
    url(r'^tut_detail/',add_tut_like,name="like_tutorial"),
    url(r'^tut_comment/',Tut_Comment_Update,name="tut_comment"),
    url(r'^news_comment/',News_Comment_Update,name="news_comment"),
    url(r'^add_tutorial/',add_tutorial.as_view(),name="add_tutorial"),
    url(r'^modify_tut/(?P<pk>[-\w]+)/$',Update_Tut.as_view(),name="update_tut"),
    url(r'^modify_news/(?P<pk>[-\w]+)/$',Update_News.as_view(),name="update_news"),
    url(r'^list_my_aricles/',List_User_Articles,name="list_my_articles"),
    url(r'^add_article/',add_article.as_view(),name="add_article"),
    url(r'^search/',search_item,name='search'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
