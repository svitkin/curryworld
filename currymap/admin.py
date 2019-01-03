from django.contrib.gis import admin
from .models import HistoryMarker
from leaflet.admin import LeafletGeoAdmin

class HistoryAdmin(LeafletGeoAdmin):
    list_display = ('title', 'geometry')

admin.site.register(HistoryMarker, HistoryAdmin)