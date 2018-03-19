from unittest import TestCase
from app import app
import json

class TestHome(TestCase):
    """Testing the home end point"""
    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, World'})

