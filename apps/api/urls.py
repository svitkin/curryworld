from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # API List view
    path('', views.ListMap.as_view()),
    # API Detail view
    path('<pk>/', views.DetailMap.as_view(), name='history-detail'),
]