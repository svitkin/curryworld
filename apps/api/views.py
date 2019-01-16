# Create your views here.
from rest_framework import generics
from django.shortcuts import get_object_or_404, render

from .models import HistoryMarker
from .serializers import HistoryMarkerSerializer
import sys
import logging

logger = logging.getLogger(__name__)

class ListMap(generics.ListCreateAPIView):
    queryset = HistoryMarker.objects.all()
    serializer_class = HistoryMarkerSerializer


class YearMap(generics.ListAPIView):
    serializer_class = HistoryMarkerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned history markers to a given year,
        by filtering against a `year` query parameter in the URL.
        """
        queryset = HistoryMarker.objects.filter(year_int=self.kwargs['year'])
        return queryset