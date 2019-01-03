from django.urls import path
from . import views


app_name = 'currymap'

urlpatterns = [
    # map history detail view
    path('<historical_title>/', views.historyDetailView, name='history-detail'),
]