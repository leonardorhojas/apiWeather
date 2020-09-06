from django.contrib.auth.models import User
from rest_framework import serializers
from weathermap.models import Weather


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ['City', 'CountryShortname']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', ]
