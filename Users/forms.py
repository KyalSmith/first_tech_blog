# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2']

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name:'
            self.fields['email'].label = 'Email:'


class User_Update_Form(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']










    '''def clean_password(self):

        if self.password != self.password2:
            raise forms.ValidationError("Passwords do NOT match!")'''


