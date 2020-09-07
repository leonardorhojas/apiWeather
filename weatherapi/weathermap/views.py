from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from rest_framework.response import Response

from utils.weatherdata import retrieve_weather_data
from .serializers import WeatherSerializer

# Default Variables for the end point and the cached time = 2 minutes
DEFAULT_CITY = getattr(settings, 'DEFAULT_CITY')
DEFAULT_COUNTRY = getattr(settings, 'DEFAULT_COUNTRY')
CACHED_TIME = getattr(settings, 'CACHED_TIME')


class WeatherViewSet(viewsets.ViewSet):
    """
    API ViewSet that supports Weather retrieving data from http://api.openweathermap.org/
    """
    serializer_class = WeatherSerializer

    @method_decorator(cache_page(CACHED_TIME))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        """
        Retrieve Weather data for a specified city & country. there are 2 decorators specifying the Cached time
        for the enppoint
        :param request:
        :return: object with weather data
        """
        # get information from os env variables for default city & country
        city = request.query_params.get('city', DEFAULT_CITY)
        country = request.query_params.get('country', DEFAULT_COUNTRY)
        # request the data to the http://api.openweathermap.org/ endpoint
        api_data = retrieve_weather_data(city=city, country=country)
        # parse data to the desired format
        serializer = WeatherSerializer(api_data)
        result = Response(serializer.data)
        # includes content-type to the headers
        result['Content-Type'] = 'application/json'
        return result
