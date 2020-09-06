from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from weathermap.serializers import UserSerializer, WeatherSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from utils.weatherdata import retrieve_weather_data
from weathermap.models import Weather

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Weather.QuerySet.all()
    #queryset = retrieve_weather_data('Bogota', 'CO')
    serializer_class = WeatherSerializer

