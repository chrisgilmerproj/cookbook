from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'recipes.views.recipe_list', name="recipe_list"),
    url(r'^random/$', 'recipes.views.recipe_random', name="recipe_random"),
    url(r'^(?P<slug>[\w-]+)/$', 'recipes.views.recipe_detail', name="recipe_detail"),
)
