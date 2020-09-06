from django.contrib.auth.models import User,  Weather
from django.shortcuts import get_object_or_404
from weatherapi.weathermap.serializers import UserSerializer, WeatherSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from weatherapi.utils.weatherdata import retrieve_weather_data

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = retrieve_weather_data()
    serializer_class = UserSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = WeatherSerializer

