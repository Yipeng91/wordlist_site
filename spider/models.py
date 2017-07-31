# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Site_info(models.Model):
    site_name = models.CharField(max_length = 100)
    site_url = models.CharField(max_length = 200)
    site_url_map = models.ForeignKey('Url_list_aready')
    


class Url_list_aready(models.Model):
    url_name = models.CharField(max_length = 200)
    site_data = models.TextField(max_length = 60000)

class Url_list_new(models.Model):
    url_name = models.CharField(max_length = 200)
    site_status = models.BooleanField() 
