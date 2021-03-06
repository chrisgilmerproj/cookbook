from django.db import models
from django.template.defaultfilters import slugify

from recipes.models import Recipe

class Variety(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Varietal name")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

class Vineyard(models.Model):
    name = models.CharField(max_length=200, help_text="Vineyard name")
    slug = models.SlugField(editable=False, unique=True)
    url = models.URLField(verify_exists=True, help_text="Vineyard website")

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Vineyard, self).save(*args, **kwargs)

class Wine(models.Model):
    RATING_CHOICES = (
        (1, "1 - hated it"),
        (2, "2 - didn't like it"),
        (3, "3 - liked it"),
        (4, "4 - really liked it"),
        (5, "5 - loved it"),
        )

    variety = models.ForeignKey(Variety)
    vineyard = models.ForeignKey(Vineyard)

    name = models.CharField(max_length=200, help_text="Name of the wine")
    year = models.PositiveIntegerField(help_text="Year on label")
    appelation = models.CharField(max_length=200, blank=True, help_text="Region of wine")
    notes = models.TextField(blank=True, help_text="Helpful notes")
    inventory = models.IntegerField(default=0, help_text="Number in inventory")
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True, help_text="Overall impression")
    
    composition = models.TextField(blank=True, help_text="Composition of blended wines")
    aroma = models.TextField(blank=True, help_text="Primary and secondary aromas")
    bouquet = models.TextField(blank=True, help_text="Tertiary aromas")

    alcohol = models.FloatField(blank=True, null=True, help_text="Alcohol by Volume")
    sulfites = models.BooleanField(default=False, help_text="Contains Sulfites")
    ta = models.FloatField("TA", blank=True, null=True, help_text="titratable acidity")
    ph = models.FloatField("pH", blank=True, null=True, help_text="pH")
    aging = models.CharField(max_length=200, blank=True, help_text="Notes on aging")
    skin_contact = models.CharField(max_length=200, blank=True, help_text="Duration of skin contact")

    class Meta:
        ordering = ['variety','name',]

    def __unicode__(self):
        return "%s %s %s, %s" % (self.name, self.variety, self.year, self.vineyard)

class WinePairing(models.Model):
    recipe = models.ForeignKey(Recipe)
    wine = models.ForeignKey(Wine)
    date  = models.DateField()
    notes = models.TextField(help_text="Notes about the pairing")

    class Meta:
        ordering = ['-date',]

    def __unicode__(self):
        return "%s with %s" % (self.recipe, self.wine)
