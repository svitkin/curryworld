# Create your models here.
from django.db import models
from django.contrib.gis.db import models as geo_models

class HistoryMarker(models.Model):

    hmarker_id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    date_float = models.FloatField(null = True)
    date_string = models.CharField(max_length=256, null = True)
    picture = models.ImageField(null = True)
    geometry = geo_models.PointField()

    def __unicode__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url


# TODO: Change historymarker model; add resources, videos, recipes, and more (make sure model still makes sense)
# TODO: Add years model? Mainly for frontend purposes... not sure how much backend logic there is
# TODO: Add lines model? Can this be calculated in postgis or leaflet? Would be useful for trade routes and connections between countries