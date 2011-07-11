import itertools
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from recipes.models import Ingredient, Recipe

def recipe_list(request):
    """ View to see list of recipes """
    recipe_list = Recipe.objects.all()

    template_name = 'recipes/recipe_list.html'
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

    template_name = 'recipes/recipe_detail.html'
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

    count = int(request.GET.get('count',6))
    tag = request.GET.get('tag',None)
    if tag:
        recipes = Recipe.objects.filter(tags__icontains=tag)
    else:
        recipes = Recipe.objects.all()
    if recipes.count() < count:
        count = recipes.count()
    recipe_list = random.sample(recipes, count)

    ingredient_dict = {}
    for ing in Ingredient.objects.filter(recipe__in=recipe_list):
        short = ing.short()
        if short:
            item = "%s" % ing.item
            if item in ingredient_dict and short not in ingredient_dict[item]:
                ingredient_dict[item].append(short)
            else:
                ingredient_dict[item] = [short]
   
    ingredient_list = []
    for item, amounts in ingredient_dict.iteritems():
        ingredient_list.append((item, amounts))
    ingredient_list.sort()

    template_name = 'recipes/recipe_random.html'
    context = {
        'ingredient_list': ingredient_list,
        'recipe_list': recipe_list,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

