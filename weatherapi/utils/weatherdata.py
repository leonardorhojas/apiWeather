import requests
from django.conf import settings
import xmltodict
import json

API_TOKEN = getattr(settings, 'API_TOKEN')
API_ENDPOINT = getattr(settings, 'WEATHER_API_ENDPOINT')


def retrieve_weather_data(city, country):
    """
    return weather data from API from a City and Country specified default bogota/co
    :param city:
    :param country:
    :return: json formated weather data from /api.openweathermap.org
    """
    # pass city & country to the openweather endpoint
    country = country.lower()
    url = '%s?q=%s,%s&appid=%s&mode=xml' % (API_ENDPOINT, city, country, API_TOKEN)
    # retrieves answer from the endpoint and format it to json
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    print(data)

    # check status of the response previous to render data or raise an error
    if response.status_code == 200:
        return data.get('current')
    else:
        raise Exception('Not valid response from API http://api.openweathermap.org/ ')
