# -*- coding=utf-8 -*-
from django.conf.urls import url
from . import views

#定义路由
urlpatterns = [
    #url(r'^join',views.join),
    url(r'^login.html$|^$',views.login),
	url(r'^register.html',views.register),
	url(r'^login_check$',views.login_check),
	url(r'^register_check$',views.register_check)
	#url(r'^login.html',views.login)
]
