from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db import models



class UserMethods(User):
    def get_absolute_url(self):
        return reverse('Users:update_user', args=(self.id,))

