from django.db import models
from django.template.defaultfilters import slugify

class Measurement(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the ingredient")

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the ingredient")

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the recipe")
    slug = models.SlugField(editable=False)
    time = models.CharField(max_length=200, blank=True, help_text="Preparation Time")
    source = models.CharField(max_length=200, blank=True, help_text="Source, please include page number")
    instructions = models.TextField(help_text="Instructions for Preparation")

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.time)

    def save(self):
        self.slug = slugify(self.title)
        super(Recipe, self).save()

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)

    amount = models.CharField(max_length=20, default="1")
    measurement = models.ForeignKey(Measurement)
    item = models.ForeignKey(Item)
    preparation = models.CharField(max_length=200, blank=True, null=True, help_text="Short prep instruction")

    def __unicode__(self):
        return "%s %s %s" % (self.measurement, self.item, self.preparation)

