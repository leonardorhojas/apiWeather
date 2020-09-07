from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """
    Serializer to format output from http://api.openweathermap.org/ to specific fields in a human readable format:
    temperature is formatted to Celsius
    pressure us formatted to hpa
    humidity is formatted to %
    sunrise/sunset is formatted to HH:MM
    geo_coordinates is formatted to [lat , long]
    requested_time is formatted to YYYY-MM-DD HH:MM:SS
    wind is formated in a  human readble scale and speed of wind in m/s
    cloudines is formated in a human readable scale
    """
    location_name = serializers.SerializerMethodField('get_location_name')
    temperature = serializers.SerializerMethodField('get_temperature')
    wind = serializers.SerializerMethodField('get_wind')
    cloudiness = serializers.SerializerMethodField('get_cloudiness')
    pressure = serializers.SerializerMethodField('get_pressure')
    humidity = serializers.SerializerMethodField('get_humidity')
    sunrise = serializers.SerializerMethodField('get_sunrise')
    sunset = serializers.SerializerMethodField('get_sunset')
    geo_coordinates = serializers.SerializerMethodField('get_geo_coordinates')
    requested_time = serializers.SerializerMethodField('get_requested_time')

    def get_location_name(self, obj):
        return obj.get('city').get('@name') + ' , ' + obj.get('city').get('country')

    def get_temperature(self, obj):
        """
        Convert kelvin to celsius temperature
        :param obj:
        :return:
        """
        celsyus_temp = float(obj.get('temperature').get('@value')) - 273.15
        return '%.0f°C' % (celsyus_temp)

    def get_wind(self, obj):
        wind_name_speed = obj.get('wind').get('speed').get('@name')
        wind_value_speed = obj.get('wind').get('speed').get('@value')
        # sometimes wind_direction is not set on the API / or the Wind doesn't have a direction
        try:
            wind_direction = obj.get('wind').get('direction').get('@name')
        finally:
            wind_direction = 'No data about wind direction'
        return '%s , %s m/s, %s' % (wind_name_speed, wind_value_speed, wind_direction)

    def get_cloudiness(self, obj):
        return obj.get('clouds').get('@name')

    def get_pressure(self, obj):
        return obj.get('pressure').get('@value') + ' hPa'

    def get_humidity(self, obj):
        return obj.get('humidity').get('@value') + '%'

    def get_sunrise(self, obj):
        return obj.get('city').get('sun').get('@rise')

    def get_sunset(self, obj):
        return obj.get('city').get('sun').get('@set')

    def get_geo_coordinates(self, obj):
        return '[' + obj.get('city').get('coord').get('@lon') + ' , ' + obj.get('city').get('coord').get('@lat') + ']'

    def get_requested_time(self, obj):
        return obj.get('lastupdate').get('@value')
