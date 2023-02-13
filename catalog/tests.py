from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_number_endpoint(self):
        tests = {
            123: 200,
            12345: 200,
            100: 200,
            200: 200,
            0: 200,
            3.1415: 404,
            -5: 404,
            "test": 404,
            "string": 404,
            None: 404,
            True: 404,
        }

        for test in tests:
            with self.subTest(test):
                response = Client().get(f"/catalog/{test}/")
                self.assertEqual(response.status_code, tests[test])
