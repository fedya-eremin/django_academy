from django.test import TestCase, Client

class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,  200)
