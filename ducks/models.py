# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Duck(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	description = models.CharField(max_length=255, null=True, blank=True)
	age = models.IntegerField(default=0)
	
