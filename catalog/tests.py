from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        tests = {
            123: 200,
            12345: 200,
            3.1415: 404,
            -5: 404,
            "test": 404,
            None: 404,
            True: 404,
        }

        for test in tests:
            response = Client().get(f"/catalog/{test}")
            self.assertEqual(response.status_code,  tests[test], msg="Error "
                             f"in {test}")
