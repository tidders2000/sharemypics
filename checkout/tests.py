from django.test import TestCase, Client
from django.contrib.auth.models import User
csrf_client = Client(enforce_csrf_checks=True)
class TestViews(TestCase):

 def test_get_checkout_not_logged_in(self):
    
    c = Client()
    page = self.client.get("/checkout",follow=True)
    self.assertEqual(page.status_code,200 )
    self.assertTemplateUsed(page, "login.html")
    
