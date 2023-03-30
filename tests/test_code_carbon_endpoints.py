from unittest import TestCase
from wsgi import app

class TestCodeCarbonEndpoints(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_carbon_health_endpoint(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_carbon_partial_track_endpoint(self):
        response = self.client.get('/partial-track')
        self.assertEqual(response.status_code, 200)

    def test_carbon_track_endpoint(self):
        response = self.client.get('/endpoint-track')
        self.assertEqual(response.status_code, 200)
