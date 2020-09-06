import requests


def retrieve_weather_data(city, country_code):
    country = country_code.lower()
    _API_TOKEN = '6ae93510c3bba0425faad68bd579a41c'
    _weather_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q='
    url = _weather_api_endpoint + city + ',' + country + '&appid=' + _API_TOKEN
    response = requests.get(url)
    print(response.status_code)
    print(response.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    retrieve_weather_data('Medellin', 'CO')

