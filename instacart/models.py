# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aisles(models.Model):
    aisle_id = models.IntegerField(blank=True, null=True)
    aisle = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aisles'


class Departments(models.Model):
    department_id = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Instacart(models.Model):
    order_id = models.CharField(max_length=10, blank=True, null=True)
    product_id = models.CharField(max_length=10, blank=True, null=True)
    add_to_cart_order = models.CharField(max_length=10, blank=True, null=True)
    reordered = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instacart'


class InstacartPrior(models.Model):
    order_id = models.CharField(max_length=10, blank=True, null=True)
    product_id = models.CharField(max_length=10, blank=True, null=True)
    add_to_cart_order = models.CharField(max_length=10, blank=True, null=True)
    reordered = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instacart_prior'


class Orders(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    eval_set = models.CharField(max_length=10, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    order_dow = models.IntegerField(blank=True, null=True)
    order_hour_of_day = models.IntegerField(blank=True, null=True)
    days_since_prior_order = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)
    aisle_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class SampleSubmission(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    products = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_submission'
