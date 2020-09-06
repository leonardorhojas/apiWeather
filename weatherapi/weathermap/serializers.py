from rest_framework import serializers
from utils.formatdates import unixtime_to_date


class WeatherSerializer(serializers.Serializer):
    location_name = serializers.SerializerMethodField('get_location_name')
    temperature = serializers.SerializerMethodField('get_temperature')
    wind = serializers.SerializerMethodField('get_wind')
    cloudiness = serializers.SerializerMethodField('get_cloudiness')
    presure = serializers.SerializerMethodField('get_presure')
    humidity = serializers.SerializerMethodField('get_humidity')
    sunrise = serializers.SerializerMethodField('get_sunrise')
    sunset = serializers.SerializerMethodField('get_sunset')
    geo_coordinates = serializers.SerializerMethodField('get_geo_coordinates')
    requested_time = serializers.SerializerMethodField('get_requested_time')

    def get_location_name(self, obj):
        return obj.get('name') + ' , ' + obj.get('sys').get('country')

    def get_temperature(self, obj):
        return (str(obj.get('main').get('temp') - 273.15)) + '°'

    def get_wind(self, obj):
        return obj.get('wind')

    def get_cloudiness(self, obj):
        return obj.get('clouds')

    def get_presure(self, obj):
        return str(obj.get('main').get('pressure')) + ' hpa'

    def get_humidity(self, obj):
        return str(obj.get('main').get('humidity')) + '%'

    def get_sunrise(self, obj):
        return unixtime_to_date(float(obj.get('sys').get('sunrise')), 'hour')

    def get_sunset(self, obj):
        return unixtime_to_date(float(obj.get('sys').get('sunset')), 'hour')

    def get_geo_coordinates(self, obj):
        return '[' + str(obj.get('coord').get('lon')) + ' , ' + str(obj.get('coord').get('lat')) + ']'

    def get_requested_time(self, obj):
        return unixtime_to_date(obj.get('dt'), 'date')
