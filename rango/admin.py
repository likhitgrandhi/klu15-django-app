# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from rango.models import *
# Register your models here.

admin.site.register(Page, PageAdmin)

class NoticeboardAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows':4,'cols':40})},
    }

admin.site.register(Noticeboard, NoticeboardAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('department',)
    prepopulated_fields = {'slug': ('course_code',)}
    list_display = ('course_name', 'course_code', 'credits',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)