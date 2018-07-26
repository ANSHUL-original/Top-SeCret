# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from. models import Post,T_Model

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['name','email','phone','profession']
	search_fields = ['name','email']

class TestAdmin(admin.ModelAdmin):
	list_display = ['name','email','contact','city']
	search_fields = ['name', 'phone']
admin.site.register(Post, PostAdmin)	

admin.site.register(T_Model, TestAdmin)	
