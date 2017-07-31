# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.

def topiclist(requset):
    if 'login' in requset.session:
        return render(requset,'wordslist/topiclist.html')
    else:
        return render(requset,'user/login.html')
    '''
    if request.session['login'] == True:
        pass
	else:
        pass#return render(requset,'user/login.html')	 '''	
def newtopic(requset):
	return render(requset,'wordslist/newtopic.html')

def uploadFile(requset):
	file = requset.FILES['uploadFile']
	return HttpResponse(file)