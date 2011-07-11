
from django.shortcuts import render_to_response
from django.template import RequestContext

from drinks.models import Wine, WinePairing

def wine_list(request):

    wine_list = Wine.objects.all()

    template_name = 'drinks/wine_list.html'
    context = {
        'wine_list': wine_list,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

