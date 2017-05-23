# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from import_export import resources
from rango.models import *
from models import User
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

class NoticeboardAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows':4,'cols':40})},
    }

admin.site.register(Noticeboard, NoticeboardAdmin)
admin.site.register(StudentProfile, StudentProfileExtra)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('department',)
    prepopulated_fields = {'slug': ('course_code',)}
    list_display = ('course_name', 'course_code', 'credits',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch')


admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)

class UserResource(resources.ModelResource):
    class Meta:
        model = User
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
