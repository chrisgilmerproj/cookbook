from django.db import models
from django.template.defaultfilters import slugify

from recipes.models import Recipe

class Variety(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Varietal name")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Variety, self).save(*args, **kwargs)

class Vineyard(models.Model):
    name = models.CharField(max_length=200, help_text="Vineyard name")
    slug = models.SlugField(editable=False, unique=True)
    url = models.URLField(verify_exists=True, help_text="Vineyard website")
    region = models.CharField(max_length=200, blank=True, help_text="Regional name")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Vineyard, self).save(*args, **kwargs)

class Wine(models.Model):
    variety = models.ForeignKey(Variety)
    vineyard = models.ForeignKey(Vineyard)

    name = models.CharField(max_length=200, help_text="Name of the wine")
    year = models.PositiveIntegerField()
    alcohol = models.FloatField(blank=True, null=True, help_text="Alcohol by Volume")
    sulfites = models.BooleanField(default=False, help_text="Contains Sulfites")
    inventory = models.IntegerField(default=0, help_text="Number in inventory")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return "%s %s %s, %s" % (self.name, self.variety, self.year, self.vineyard)

class Pairing(models.Model):
    recipe = models.ForeignKey(Recipe)
    wine = models.ForeignKey(Wine)
    date  = models.DateField()

    class Meta:
        ordering = ['-date',]

    def __unicode__(self):
        return "%s with %s" % (self.recipe, self.wine)
