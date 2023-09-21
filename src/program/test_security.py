from django.test import TestCase


class ProgramSecurityTestCase(TestCase):
    def test_sayHello_shouldEscapeHtmlResponse(self):
        res = self.client.get("/sayHello/", {"name": "<script>alert(1)</script>"})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "&lt;script&gt;alert(1)&lt;/script&gt;")
