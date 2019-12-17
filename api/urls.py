from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/day-data/', views.day_data, name='daily')
]