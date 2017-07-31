# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def admin(request,id1,id2):
    return HttpResponse("还没搞好！...%s%s"%(id1,id2)) 
