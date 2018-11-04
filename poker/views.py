# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render

# Create your views here.

def index(req):
	return render(req, "poker/index.html")

def lobby(req):
	r = random.randint(0,100)
	return render(req, "poker/lobby.html", {"rand":r})
