# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import *

admin.site.register(Tutorial)
admin.site.register(Topic)
admin.site.register(NewsLikeCount)
admin.site.register(TutLikeCount)
admin.site.register(NewsArticle)
admin.site.register(TutorialComment)
admin.site.register(NewsComment)


