from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from .models import HistoryMarker

def historyDetailView(request, historical_title):
    '''
        Historical Marker view
    '''
    historical_points = get_object_or_404(HistoryMarker, title=historical_title)

    return render(request, 'currymap/history-detail.html', {"historical_points": historical_points})

