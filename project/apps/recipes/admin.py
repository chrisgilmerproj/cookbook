from django.contrib import admin
from recipes.models import Measurement, Ingredient, Item, Recipe

class IngredientInline(admin.TabularInline):
    extra = 1
    model = Ingredient

class MeasurementAdmin(admin.ModelAdmin): pass
admin.site.register(Measurement, MeasurementAdmin)

class ItemAdmin(admin.ModelAdmin): pass
admin.site.register(Item, ItemAdmin)

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline,]

admin.site.register(Recipe, RecipeAdmin)

