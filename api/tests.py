from datetime import datetime
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import index, RetrieveData, date_to_timestamp
from .weather_data import WeatherData


class TestTemplate(TestCase):

    def test_page_loads(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

        request = HttpRequest()  
        response = index(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<!doctype html>', html)  
        self.assertIn('<title>Twende Weather App</title>', html)  
        self.assertTrue(html.endswith('</html>'))  

    
class TestData(TestCase):
    def setUp(self):
        self.current_data = RetrieveData().retrieve_current_data()
        self.day_data = RetrieveData().retrieve_specific_day_data(1576702800)

        

    def test_date_timestamp_converter(self):
        date_str = '12/21/2019'
        self.tmstamp:float = date_to_timestamp(date_str)
        self.day_data = RetrieveData().retrieve_specific_day_data(int(self.tmstamp))
        assert isinstance(self.tmstamp, float)        

    def test_data_class(self):
        assert isinstance(self.current_data.time, datetime)
        assert isinstance(self.current_data.summary, str)
        assert isinstance(self.current_data.icon, str)
        assert isinstance(self.current_data.temperature, float)
        assert isinstance(self.current_data.humidity, float)
        assert isinstance(self.current_data.pressure, float)
        assert isinstance(self.current_data.wind_speed, float)
        assert isinstance(self.current_data.precipitation, float)
        assert isinstance(self.current_data.visibility, float)

    
