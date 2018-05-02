# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from services.duckService import DuckService

from . import models

# Create your views here.

def index(request):
	return render(request, 'ducks/index.html')
#end index

def store(request):
	service = DuckService()
	newDuck = service.createNewDuck()
	return render(request, 'ducks/show.html')
#end store