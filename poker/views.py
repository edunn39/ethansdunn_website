# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from logic.card import Card
from logic.deck import Deck

from django.shortcuts import render

# Create your views here.

def index(req):
	return render(req, "poker/index.html")

def lobby(req):
	r = random.randint(0,100)
	d = {}
	d["rand"] = r
	deck = Deck()
	d["p1_cards"] = deck.get_cards(2)
	d["p2_cards"] = deck.get_cards(2)
	return render(req, "poker/lobby.html", d)
