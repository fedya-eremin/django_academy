from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee")
        with self.subTest():
            # self.assertEqual(response.content, "I'm a teapot: /coffee")
            self.assertEqual(response.status_code, 418)

        with self.subTest("content"):
            self.assertEqual(response.content.decode("utf-8"), "Я - чайник!")
