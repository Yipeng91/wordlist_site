from django.conf.urls import url,include
from . import views
#create urls
urlpatterns = [
	url('^topiclist.html',views.topiclist),
	url('^newtopic.html',views.newtopic),
	url('^uploadFile',views.uploadFile)
]