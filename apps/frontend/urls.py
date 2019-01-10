from django.urls import path
from . import views
from django.views import generic


app_name = 'frontend'

urlpatterns = [
    # map history detail view
    path('', generic.TemplateView.as_view(template_name='frontend/introduction.html'), name='intro'),
    path('learnmore/', generic.TemplateView.as_view(template_name='frontend/learnmore.html'), name='learnmore'),
    path('map/', views.HistoryTestPage.as_view(), name='historytest'),
]