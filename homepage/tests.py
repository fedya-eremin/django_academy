from django.test import Client, TestCase

import environ


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee")
        with self.subTest("teapot"):
            # self.assertEqual(response.content, "I'm a teapot: /coffee")
            self.assertEqual(response.status_code, 418)

        with self.subTest("content"):
            self.assertEqual(response.content.decode("utf-8"), "Я - чайник!")

    def test_reverse_ru_middleware(self):
        """tests my middleware"""
        env = environ.Env(ENABLE_REVERSE_RU_MIDDLEWARE=(bool, False))
        is_enabled = env("ENABLE_REVERSE_RU_MIDDLEWARE")
        tests = {
            "человек на луне": "<body>кеволеч ан енул</body>",
            "яндекс браузер": "<body>скедня резуарб</body>",
            "google": "<body>google</body>",
            "гугл chrome": "<body>лгуг chrome</body>",
            "the quick brown fox": "<body>the quick brown fox</body>",
            "11//23.31df11мама_мыла123123раму;;!3": "<body>11//23.31d"
            "f11амам_алым123123умар;;!3</body>",
            True: "<body>True</body>",
            None: "<body>None</body>",
        }
        if is_enabled is True:  # if middleware is enabled
            for test in tests:
                with self.subTest(test):
                    for i in range(9):
                        response = self.client.get(f"/test/{test}")
                        self.assertEqual(
                            response.content.decode("utf-8"),
                            f"<body>{test}</body>",
                        )
                    response = self.client.get(f"/test/{test}")
                    self.assertEqual(
                        response.content.decode("utf-8"), tests[test]
                    )
        else:  # otherwise
            for test in tests:
                with self.subTest(test):
                    for i in range(10):
                        response = self.client.get(f"/test/{test}")
                        self.assertEqual(
                            response.content.decode("utf-8"),
                            f"<body>{test}</body>",
                        )
