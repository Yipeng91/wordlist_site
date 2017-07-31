# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader,RequestContext
from instacart.models import Aisles,Departments,DjangoMigrations,Instacart,InstacartPrior,Orders,Products,SampleSubmission
#from django.short  import render
 
def hello(request):
    print(Aisles.objects.all()[1].aisle_id)
    template = loader.get_template('mysite/index.html')
    if request.COOKIES.has_key('username') and ('username' in request.session):# or request.COOKIES['username']
        if request.session['username'] == request.COOKIES['username']: 
            cookies = request.session['username']
            logStatus = '注销'
        else:
            cookies = '未登陆'
            logStatus = '登陆'
    else:
        cookies = '未登录！'
        logStatus = '登陆'
    context = {'username':cookies,'logStatus':logStatus}
    context['QuerySet'] = Aisles.objects.all()
    return HttpResponse(template.render(context))
def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context))
def login(request):
    template = loader.get_template('mysite/login.html')
    context =  {}
    return HttpResponse(template.render(context))
def check(request):
    user = request.POST.get('username')
    print(type(user),type('哈哈哈'))
    password = request.POST.get("password")
    context = {}
    if user == u'哈哈哈' and password == '123456':
        template = loader.get_template('mysite/succeed.html')
        redirect = HttpResponseRedirect('/')
        request.session['username']='sdlkfjlkasdjfsakdjf'
        redirect.set_cookie('username','sdlkfjlkasdjfsakdjf')
        return redirect
    else:
        template = loader.get_template('mysite/error.html')
        return HttpResponse(template.render(context)) 
    #context = {'user':user,'password':password}
def login_ajax_check(request):
    username = request.GET.get('username')
    passsword = request.GET.get('password')
    if username == 'admin' and password == '123456':
        return JsonResponse({'status':'succeed'})
    else:
        return JsonResponse({'status':'error'})
def show_add(request):
    template = loader.get_template('mysite/succeed.html')
    context = {'res':request.COOKIES['res']}
    return  HttpResponse(template.render(context))
def query(request):
    template = loader.get_template('mysite/query.html')
    context = {}
    return HttpResponse(template.render(context))


