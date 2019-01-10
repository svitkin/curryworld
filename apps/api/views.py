# Create your views here.
from rest_framework import generics
from django.shortcuts import get_object_or_404, render

from .models import HistoryMarker
from .serializers import HistoryMarkerSerializer

from rest_framework.renderers import JSONRenderer

class ListMap(generics.ListCreateAPIView):
    queryset = HistoryMarker.objects.all()
    serializer_class = HistoryMarkerSerializer
    renderer_classes = (JSONRenderer, )


class DetailMap(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoryMarker.objects.all()
    renderer_classes = (JSONRenderer, )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(hmarker_id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    serializer_class = HistoryMarkerSerializer