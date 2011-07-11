from django.contrib import admin

from models import *

admin.site.register(Variety)

class VineyardAdmin(admin.ModelAdmin):
    list_display = ['name','url','region',]

admin.site.register(Vineyard, VineyardAdmin)

class WineAdmin(admin.ModelAdmin):
    list_display = ['name','variety','year','vineyard','alcohol','sulfites','inventory']
    list_editable = ['inventory',]

admin.site.register(Wine, WineAdmin)

class PairingAdmin(admin.ModelAdmin):
    list_display = ['recipe','wine','date',]

admin.site.register(Pairing, PairingAdmin)
