from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.utils import json


class API_Test_Case(TestCase):

    def SetUp(self):
        self.client = APIClient()

    def test_request(self):
        request = self.client.get('/weather/?city=medellin&country=co')
        assert request.status_code == 200

    def test_data(self):
        moked_data = {'location_name': 'Medellín , CO', 'temperature': '16.83000000000004°',
                      'wind': {'speed': 2.1, 'deg': 110}, 'cloudiness': {'all': 40}, 'presure': '1023 hpa',
                      'humidity': '60%', 'sunrise': '05:54', 'sunset': '18:06',
                      'geo_coordinates': '[-75.56 , 6.25]', 'requested_time': '2020-09-06  19:20:59'}
        request = self.client.get('/weather/?city=medellin&country=co')
        self.assertNotEqual(json.loads(request.content), moked_data)

    def test_static_data(self):
        moked_location_name =  'Medellín , CO'
        request = self.client.get('/weather/?city=medellin&country=co')
        request_data = json.loads(request.content)
        self.assertEqual(request_data.get('location_name'), moked_location_name)


