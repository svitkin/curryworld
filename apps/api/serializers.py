from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import HistoryMarker


class HistoryMarkerSerializer(GeoFeatureModelSerializer):
    class Meta:
        fields = "__all__"
        geo_field = "geometry"
        model = HistoryMarker