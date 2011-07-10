from django.contrib import admin
from recipes.models import Measurement, Ingredient, Item, Recipe

class MeasurementAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Measurement, MeasurementAdmin)

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Item, ItemAdmin)

class IngredientInline(admin.TabularInline):
    extra = 1
    model = Ingredient
    raw_id_fields = ['item',]

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [
            'name','time','serves','leftovers','source','source_url','tags'
        ]}),
        (None, {'fields': [
            'equipment','instructions','health',
        ]}),
    )
    inlines = [IngredientInline,]
    list_display = ['name','time','serves','leftovers','source','tags',]
    list_editable = ['time','serves','leftovers','tags']

admin.site.register(Recipe, RecipeAdmin)
