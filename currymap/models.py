from django.db import models
from django.contrib.gis.db import models as geo_models

class HistoryMarker(models.Model):

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