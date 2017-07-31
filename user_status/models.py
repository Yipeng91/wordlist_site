# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfoManager(models.Manager):
    def create(self,username,password,frist_name,last_name,email,is_superuser=0,is_staff=0,is_active=1):
    	user = self.model()
    	user.username =username
    	user.password = password
    	user.frist_name = frist_name
    	user.email = email
    	user.is_superuser = is_superuser
    	user.is_staff = is_staff
    	user.is_active = is_active
    	return user



class User(models.Model):
    username = models.CharField(max_length = 128,unique = True)
    password = models.CharField(max_length = 128)
    last_login = models.DateField(auto_now = True)
    frist_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length= 254)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default = False)
    class Mate:
        db_table = 'user_info'
    user = UserInfoManager()


