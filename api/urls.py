from django.conf.urls import url,include

from .views import *


urlpatterns = [
    url(r'tutorial/postings/(?P<pk>[-\w]+)/$',Tutorial_Post_RUD_view.as_view(),name='post-tut-rud'),
    url(r'tutorial/create/$',Tutorial_Post_List_Create_view.as_view(),name='post-tut-create'),
    url(r'article/postings/(?P<pk>[-\w]+)/$',Article_Post_RUD_view.as_view(),name='post-art-rud'),
    url(r'article/create/$',Article_Post_List_Create_view.as_view(),name='post-art-create'),
    url(r'tutorial/posts/',Tutorial_Get_All_Posts.as_view(),name='post-tut-all'),
    url(r'article/posts/',Article_Get_All_Posts.as_view(),name='post-article-all'),
]
