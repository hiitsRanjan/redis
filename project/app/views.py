from django.shortcuts import render
from .models import Recipe
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings , 'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_recipe(filter_recipe=None):
    if filter_recipe:
        recipes = Recipe.objects.filter(name__contains=filter_recipe)
    else:
        recipes = Recipe.objects.all()
    return recipes


def index(request):
    filter_recipe =  request.GET.get('recipe')
    if cache.get(filter_recipe):
        recipe = cache.get(filter_recipe)
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
        else:
            recipe = get_recipe()
    context = {'recipe':recipe}
    return render(request,'index.html',context)


def show(request,id):
    recipe = Recipe.objects.get(id=id)
    context = {"recipe":recipe}
    return render(request,"show.html",context)