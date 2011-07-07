import itertools
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from recipes.models import Ingredient, Recipe

def recipe_list(request):
    """ View to see list of recipes """
    recipe_list = Recipe.objects.all()

    template_name = 'recipe_list.html'
    context = {
        'recipe_list': recipe_list,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

def recipe_detail(request, slug):
    """ View to see a recipe """
    recipe_detail = Recipe.objects.get(slug=slug)

    template_name = 'recipe_detail.html'
    context = {
        'recipe': recipe_detail,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

def recipe_random(request):
    """ View to see list of recipes """
    recipes = Recipe.objects.all()
    count = 6
    if recipes.count() < count:
        count = recipes.count()
    recipe_list = random.sample(recipes, count)

    items = [(ing.item.name,ing) for ing in Ingredient.objects.filter(recipe__in=recipes)]
    items.sort()
    ingredient_list = [x[1] for x in items]

    template_name = 'recipe_random.html'
    context = {
        'ingredient_list': ingredient_list,
        'recipe_list': recipe_list,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

