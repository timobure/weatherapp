import json
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json
from darksky import forecast
from django.conf import settings

@dataclass_json
@dataclass
class WeatherData:
    """
    Container for retrieved data
    """
    time: datetime
    summary: str
    icon: str
    temperature: float
    humidity: float
    pressure: float
    wind_speed: float
    precipitation: float
    uv_index: float
    visibility: float


class RetrieveData:
    """
    Retrieves and stores the weather data
    """
    def __init__(self):
        self.key: str = settings.DARK_SKY_API_KEY
        self.latitude: float = 1.2921
        self.longitude: float = 36.8219
        self.units = 'si'
        self.data: CurrentData

    def retrieve_current_data(self)->WeatherData:
        nairobi: forecast.Forecast = forecast(
                                                self.key, 
                                                self.latitude, 
                                                self.longitude, 
                                                units=self.units,
                                                )
        data = WeatherData(  
            datetime.fromtimestamp(nairobi.currently['time']),    
            nairobi.currently['summary'],
            nairobi.currently['icon'],
            float(nairobi.currently['temperature']),
            float(nairobi.currently['humidity']),
            float(nairobi.currently['pressure']),
            float(nairobi.currently['windSpeed']),
            float(nairobi.currently['precipIntensity']),
            float(nairobi.currently['uvIndex']),
            float(nairobi.currently['visibility'])
            )
        return data

    def retrieve_specific_day_data(self, day: float)->json:
        nairobi: forecast.Forecast = forecast(
                                                self.key, 
                                                self.latitude, 
                                                self.longitude, 
                                                units=self.units,
                                                time=day
                                                )
        data = WeatherData(  
            datetime.fromtimestamp(nairobi.currently['time']),    
            nairobi.currently['summary'],
            nairobi.currently['icon'],
            float(nairobi.currently['temperature']),
            float(nairobi.currently['humidity']),
            float(nairobi.currently['pressure']),
            float(nairobi.currently['windSpeed']),
            float(nairobi.currently['precipIntensity']),
            float(nairobi.currently['uvIndex']),
            float(nairobi.currently['visibility'])
            )
        data = data.to_dict()
        assert isinstance(data, str)
        return data


