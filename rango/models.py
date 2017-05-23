# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from rango.choices import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, choices=DEPARTMENTS_CHOICES, default="")
    batch = models.CharField(max_length=100, choices=BATCH_CHOICES, default="")

    def __str__(self):
        return self.name + '-' + self.batch



class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_id = models.CharField(max_length=10, blank=True)
    department = models.ForeignKey(Department)


    def __str__(self):
        return self.registration_id

class StudentProfileExtra(admin.ModelAdmin):
    list_display = ('user', 'registration_id', 'department')


class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(max_length=None)
    department = models.ManyToManyField(Department)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_code)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.course_name


class Page(models.Model):
    category = models.ForeignKey(Category)
    course = models.ForeignKey(Course, default="")
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'course',)



class Noticeboard(models.Model):
    notice = models.CharField(max_length=500)
    post = models.TextField()
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return self.notice


