from django.test import Client, TestCase, modify_settings


class StaticUrlTests(TestCase):
    def setUp(self):
        self.tests = {
            "человек на луне": "<body>кеволеч ан енул</body>",
            "яндекс браузер": "<body>скедня резуарб</body>",
            "google": "<body>google</body>",
            "гугл chrome": "<body>лгуг chrome</body>",
            "the quick brown fox": "<body>the quick brown fox</body>",
            "11//23.31df11мама_мыла123123раму;;!3": (
                "<body>11//23.31df11амам_алым123123умар;;!3</body>"
            ),
            True: "<body>True</body>",
            None: "<body>None</body>",
        }

    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee")
        with self.subTest("teapot"):
            self.assertEqual(response.status_code, 418)

        with self.subTest("content"):
            self.assertEqual(response.content.decode("utf-8"), "Я - чайник!")

    @modify_settings(
        MIDDLEWARE={
            "append": "myserver.middleware.ReverseRuMiddleware",
        }
    )
    def test_reverse_ru_middleware_on(self):
        for test in self.tests:
            with self.subTest(test):
                for i in range(9):
                    response = self.client.get(f"/test/{test}")
                    self.assertEqual(
                        response.content.decode("utf-8"),
                        f"<body>{test}</body>",
                    )
                response = self.client.get(f"/test/{test}")
                self.assertEqual(
                    response.content.decode("utf-8"), self.tests[test]
                )

    @modify_settings(
        MIDDLEWARE={
            "remove": "myserver.middleware.ReverseRuMiddleware",
        }
    )
    def test_reverse_ru_middleware_off(self):
        for test in self.tests:
            with self.subTest(test):
                for i in range(10):
                    response = self.client.get(f"/test/{test}")
                    self.assertEqual(
                        response.content.decode("utf-8"),
                        f"<body>{test}</body>",
                    )
