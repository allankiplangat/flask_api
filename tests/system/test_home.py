from tests.system.base_test import BaseTest
import json

class TestHome(BaseTest):
    """Testing the home end point"""
    def test_home(self):
        with self.app() as client:
            resp = client.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, World'})

