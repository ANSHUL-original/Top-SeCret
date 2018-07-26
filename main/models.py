# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	name=models.CharField(max_length=50)
	email= models.EmailField(max_length=50)
	phone= models.CharField(max_length=50)
	profession= models.CharField(max_length=50)

class T_Model(models.Model):
	name= models.CharField(max_length=30)
	email= models.CharField(max_length=30) 
	contact =models.CharField(max_length=15)
	city = models.CharField(max_length=15)
	#nationality = models.CharField(max_length=20) 