# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader,RequestContext
from user_status.models import  User
from django.contrib.auth.hashers import make_password,check_password

# Create your views here

def join(request):
    template = loader.get_template('user/join.html')
    context = {}
    return   HttpResponse(template.render(context))
def login(request):
    template = loader.get_template('user/login.html')
    context = {}
    return   HttpResponse(template.render(context))
def register(request):
    template = loader.get_template('user/register.html')
    context = {}
    return   HttpResponse(template.render(context))
def login_check(request):
    user = request.POST.get('log_username')
	
    print(type(user),type('哈哈哈'))
    password = make_password(request.POST.get("log_password"))
    context = {}
    if User.user.filter(username=user).filter(password=password):
        template = loader.get_template('mysite/succeed.html')
        redirect = HttpResponseRedirect('/')
        request.session['login']=True
        redirect.set_cookie('name','')
        return redirect
    else:
        template = loader.get_template('mysite/error.html')
        return HttpResponse(template.render(context)) 
def register_check(request):
	username = request.POST.get('username')
	'''a = User
	if a.get_queryset().filter(username==username):
		context = '<h1>已经注册</h1>'
		return HttpResponse(context)'''
	password = make_password(request.POST.get('password'))
    
	firstname = request.POST.get('first_name')
	lastname = request.POST.get('last_name')
	email = request.POST.get('email')
	user =User.user.create(username,password,firstname,lastname,email)
	user.save()
	return HttpResponse('<h1>哈哈哈哈</h1>')

	