from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'wine_list/$', 'drinks.views.wine_list', name="wine_list"),
)
