from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^recipes/$', 'recipes.views.recipe_list', name="recipe_list"),
    url(r'^recipes/random/$', 'recipes.views.recipe_random', name="recipe_random"),
    url(r'^recipes/(?P<slug>[\w-]+)/$', 'recipes.views.recipe_detail', name="recipe_detail"),
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="home"),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
