from django.test import TestCase, Client

csrf_client = Client(enforce_csrf_checks=True)

class TestViews(TestCase):
        """
        tests to run against cart
        
        """
# Create your tests here.
def test_cart_view(self):
        page = self.client.get("/cart/", follow=True)
        self.assertEqual(page.status_code, 200)
        
def test_add_to_cart(self):
    
         c = Client()
         page = c.get('add_to_cart', {'id': 1})
         self.assertEqual(page.status_code, 200)

def test_add_to_cart_nothing(self):
         c = Client()
         page = c.get('add_to_cart', {})
         self.assertEqual(page.status_code, 200)