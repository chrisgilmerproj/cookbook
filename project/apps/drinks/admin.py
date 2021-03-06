from django.contrib import admin

from models import *

admin.site.register(Variety)

class VineyardAdmin(admin.ModelAdmin):
    list_display = ['name','url',]

admin.site.register(Vineyard, VineyardAdmin)

class WineAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [
            ('variety','vineyard',),
            ('name','appelation','year',),
            ('inventory','rating',),
            'notes',
        ]}),
        ('Chemistry', {'fields': [
            ('alcohol','sulfites',),
            ('ta','ph',),
            ('aging','skin_contact',),
        ]}),
        ('Composition', {'fields': [
            'composition','aroma','bouquet',
        ]}),
    )
    list_display = ['name', 'variety', 'appelation', 'year', 'vineyard', 'rating', 'inventory']
    list_editable = ['inventory',]
    list_filter = ['year', 'appelation', 'rating',]
    search_fields = ['name', 'appelation', 'year',]

admin.site.register(Wine, WineAdmin)

class WinePairingAdmin(admin.ModelAdmin):
    list_display = ['recipe','wine','date',]
    raw_id_fields = ['recipe','wine',]

admin.site.register(WinePairing, WinePairingAdmin)
