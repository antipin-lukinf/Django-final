from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipes, Category


def index(request):
    recipes = Recipes.objects.all()
    categories = Category.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Список рецептов',
        'categories': categories,
    }
    return render(request, template_name='recipes/index.html', context=context)


def get_category(request, category_id):
    recipes = Recipes.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'recipes/category.html', {'recipes': recipes, 'categories': categories, 'category': category})