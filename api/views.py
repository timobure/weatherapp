import asyncio
from datetime import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .weather_data import WeatherData, RetrieveData


def date_to_timestamp(date: str)->float:
    date_timestamp: float = datetime.strptime(date, '%m/%d/%Y').timestamp()
    return date_timestamp


def index(request):
    data: CurrentData = RetrieveData().retrieve_current_data()
    context: dict = {'data': data}
    return render(request, 'api/index.html', context)


def day_data(request):
    day: str = request.GET.get('day')
    tmstamp = date_to_timestamp(day)
    data: json = RetrieveData().retrieve_specific_day_data(int(tmstamp))
    return JsonResponse(data)






