from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipes


def index(request):
    recipes = Recipes.objects.all()
    rec = '<h1>Список рецептов</h1>'
    for item in recipes:
        rec += f'<div><p>{item.title}</p></div>'

    return HttpResponse(rec)
