# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from django.contrib.auth import (
    views as auth_views,
    logout,
    login,
    authenticate,
    get_user_model,
    update_session_auth_hash)
from .forms import User_Update_Form
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)



# Create your views here.

class Signup(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('blog_content:home')
    template_name = "Users/signup.html"

def SignOut(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('blog_content:home'))


def SignIn(request):

    logged_in = False

    if request.method == "POST" and logged_in == False:

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:
                login(request,user)
                logged_in = True
                return HttpResponseRedirect(reverse_lazy('blog_content:home'))

            else:

                return HttpResponse("Account not Active!")

        else:

            print("Failed Login Attempt")
            print("Username: {} and password: {}".format(username, password))
            return render(request, 'Users/signin.html',{"message":"Either User does not exist or credentials are incorrect!"})

    else:
        return render(request, 'Users/signin.html')





def update_user(request):

    if request.method=="POST":

        update_form = User_Update_Form(request.POST,instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return redirect('Users/update_user.html')


    else:

        update_form = User_Update_Form(instance = request.user)
        return render(request,'Users/update_user.html',{'form':update_form})







def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('blog_content:home')


    else:
        form = PasswordChangeForm(data=request.POST,user=request.user)

        args = {'form':form}
        return render(request,'Users/update_password.html',args)
