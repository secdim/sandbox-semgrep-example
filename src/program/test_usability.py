from django.test import TestCase


class ProgramTestCase(TestCase):
    def test_should_say_hello(self):
        res = self.client.get("/sayHello/", {"name": "John"})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Hello, John")

    def test_when_request_status_should_return_200(self):
        res = self.client.get("/status")
        self.assertEqual(res.status_code, 200)
