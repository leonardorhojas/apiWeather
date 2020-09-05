# apiWeather

API to request Weather data from http://api.openweathermap.org/

Support the following endpoints
    1. GET /weather?city=$City&country=$
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
