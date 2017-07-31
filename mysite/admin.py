from django.contrib import admin
from spider.models import Site_info,Url_list_aready,Url_list_new
from .models import GoodsInfo
class Site_info_admin(admin.ModelAdmin):
    list_display = ['id','site_name','site_url','site_url_map_id']

admin.site.register(Site_info,Site_info_admin)
admin.site.register(GoodsInfo)