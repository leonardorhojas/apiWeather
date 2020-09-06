import requests
from django.conf import settings

API_TOKEN = getattr(settings, 'API_TOKEN')
API_ENDPOINT = getattr(settings, 'WEATHER_API_ENDPOINT')


def retrieve_weather_data(city, country):
    # TBD System Variables

    country = country.lower()
    url = API_ENDPOINT + city + ',' + country + '&appid=' + API_TOKEN
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        raise Exception('Not valid response from API openweather')
