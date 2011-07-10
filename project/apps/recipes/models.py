from django.db import models
from django.template.defaultfilters import slugify

from tagging.fields import TagField

class Measurement(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the ingredient")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the ingredient")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Item, self).save(*args, **kwargs)

class Recipe(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the recipe")
    slug = models.SlugField(editable=False, unique=True)
    time = models.CharField(max_length=200, blank=True, help_text="Preparation Time")
    serves = models.PositiveIntegerField(default=1, blank=True, help_text="Number of servings")
    leftovers = models.BooleanField(default=False, help_text="Makes Leftovers")
    source = models.CharField(max_length=200, blank=True, help_text="Source, please include page number")
    source_url = models.URLField(verify_exists=True, blank=True)
    equipment = models.TextField(blank=True, help_text="Equipment for Preparation")
    instructions = models.TextField(help_text="Instructions for Preparation")
    health = models.TextField(blank=True, help_text="Related health facts")

    tags = TagField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)

    order = models.PositiveIntegerField(blank=True, null=True)
    multiplier = models.PositiveIntegerField(default=1)
    amount = models.CharField(max_length=20, default="1")
    measurement = models.ForeignKey(Measurement, blank=True, null=True)
    item = models.ForeignKey(Item)
    preparation = models.CharField(max_length=200, blank=True, help_text="Short prep instruction")
    optional = models.BooleanField(default=False)

    class Meta:
        ordering = ['order','id']

    def __unicode__(self):
        name = ""
        if self.multiplier > 1:
            name += "%sx " % self.multiplier
        if self.amount != '1':
            name += "%s " % (self.amount)
        if self.amount == '1' and self.measurement:
            name += "%s " % (self.amount)
        if self.measurement:
            name += "%s " % (self.measurement)
        name += "%s %s" % (self.item, self.preparation)
        if self.optional:
            name += "*"
        return name

    def short(self):
        name = ""
        if self.multiplier > 1:
            name += "%sx " % self.multiplier
        if self.amount != '1':
            name += "%s " % (self.amount)
        if self.amount == '1' and self.measurement:
            name += "%s " % (self.amount)
        if self.measurement:
            name += "%s " % (self.measurement)
        name += "%s" % (self.preparation)
        if self.optional:
            name += "*"
        return name

