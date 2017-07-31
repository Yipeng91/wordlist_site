#coding=utf-8
#导入urls包
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index',views.index),
    url(r'^admin(?P<id1>\d+)(?P<id2>\w+)/$',views.admin)
    ]
