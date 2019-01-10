from django.shortcuts import render
from django.views import generic

# Create your views here.
# TODO: Maybe remove if not developed or seems like it should be developed in the near future
class HistoryTestPage(generic.TemplateView):
    def get(self, request):
        return render(request, 'frontend/historytest.html')