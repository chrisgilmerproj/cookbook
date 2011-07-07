from django.shortcuts import render_to_response
from django.template import RequestContext

from recipes.models import Recipe

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
