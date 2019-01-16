from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # API List view
    path('', views.ListMap.as_view()),
    # API Detail view
    path('<year>/', views.YearMap.as_view(), name='history-detail'),
]

# TODO: make it like other api requests, with parameters?