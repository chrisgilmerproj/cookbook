from django.contrib import admin
from recipes.models import Measurement, Ingredient, Item, Recipe

class IngredientInline(admin.TabularInline):
    extra = 1
    model = Ingredient

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

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Measurement)
admin.site.register(Item)


