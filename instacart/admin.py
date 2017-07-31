# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from instacart.models import Aisles,Departments,Instacart,InstacartPrior,Orders,Products

# Register your models here.
admin.site.register(Aisles)
admin.site.register(Departments)
admin.site.register(Instacart)
admin.site.register(InstacartPrior)
admin.site.register(Orders)
admin.site.register(Products)
