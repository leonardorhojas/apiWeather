import requests
from django.core import serializers
import requests
import json
from datetime import datetime
import tzlocal


def unixtime_to_date(unix_timestamp, type):  # TBD to decorator
    local_timezone = tzlocal.get_localzone()
    date_timestamp = datetime.fromtimestamp(unix_timestamp, local_timezone)
    # check type of conversion DRY
    date = ''
    if type == 'date':
        date = date_timestamp.strftime("%Y-%m-%d  %H:%M:%S")
    elif type == 'hour':
        date = date_timestamp.strftime("%H:%M")
    return date


def retrieve_weather_data(city, country_code):
    # TBD System Variables
    _API_TOKEN = '6ae93510c3bba0425faad68bd579a41c'
    _weather_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q='
    country = country_code.lower()
    url = _weather_api_endpoint + city + ',' + country + '&appid=' + _API_TOKEN
    response = requests.get(url)
    data = response.json()
    appdata = dict(location_name=data['name'] + ' , ' + country_code,
                   temperature=(str(data['main']['temp'] - 273.15)) + '°', wind=data['wind'], cloudiness=data['clouds'],
                   presure=str(data['main']['pressure'])+' hpa', humidity=str(data['main']['humidity']) + '%',
                   sunrise=unixtime_to_date(float(data['sys']['sunrise']), 'hour'),
                   sunset=unixtime_to_date(float(data['sys']['sunset']), 'hour'),
                   geo_coordinates='[' + str(data['coord']['lon']) + ' , ' + str(data['coord']['lat']) + ']',
                   requested_time=unixtime_to_date(data['dt'], 'date'))
    return appdata


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    retrieve_weather_data('Medellin', 'CO')
