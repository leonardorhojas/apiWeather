# API Weather
API to request Weather data from http://api.openweathermap.org/

Support the following endpoints
```bash
GET /weather?city=$City&country=$co

Response:  {
    "location_name": "Bogota, CO",
    "temperature": "17 °C", → Temp en Kelvins
    "wind": Gentle breeze, 3.6 m/s, west-northwest",  
    "cloudines": "Scattered clouds", 
    "presure": "1027 hpa",
    "humidity": "63%", 
    "sunrise": "06:07", 
    "sunset": "18:00",  
    "geo_coordinates": "[4.61, -74.08]",
    "requested_time": "2018-01-09 11:57:00" 
  }

```
 • **City** is a string. Example: Bogota

 • **Country** is a country code of two characters in lowercase. 

Example: co

a list of the country codes is available at:

https://www.iban.com/country-codes

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install API Weather, previously you should create a vertualenv.

```bash
python3 -m venv env
pip install -r requirements.txt
```

## Usage

```bash 

source env/bin/activate

cd somepath/apiWeather/weatherapi

python manage.py runserver
```
you can set the following OS ENV Variables to set some features:

# Application Settings loaded from environment variables
WEATHER_API_TOKEN = 'your openwhaterapitoken'
WEATHER_API_ENDPOINT = should be: 'http://api.openweathermap.org/data/2.5/weather')

# Defatul Preseted variables to reach API and set a cache of 2 minutes
DEFAULT_CITY= 'bogota')
DEFAULT_COUNTRY = 'co'
CACHED_TIME = '60 * 2'


## License
[MIT](https://choosealicense.com/licenses/mit/)
