# API Weather
API to request Weather data from http://api.openweathermap.org/

Support the following endpoints
```bash
GET /weather?city=$City&country=$co

Response:  {
    "location_name": "Bogota, CO",
    "temperature": "17 °C", → Temp en Kelvins
    "wind": Gentle breeze, 3.6 m/s, west-northwest",  → API(??)
    "cloudines": "Scattered clouds", → API(???)
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


## License
[MIT](https://choosealicense.com/licenses/mit/)