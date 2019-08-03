from django.test import TestCase, Client
from django.contrib.auth.models import User
csrf_client = Client(enforce_csrf_checks=True)
from .models import Order, OrderLineItem

class TestViews(TestCase):

 def test_get_checkout_not_logged_in(self):
    
    c = Client()
    page = self.client.get("/checkout",follow=True)
    self.assertEqual(page.status_code,200 )
    self.assertTemplateUsed(page, "login.html")
    
 def test_get_checkout_logged_in(self):
       test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
       test_user1.save()
       
       login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
       response = self.client.get('/checkout/')
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'checkout.html')
        
        
 def test_order_form(self):
  order=Order(full_name='mr Test', phone_number='00000000000', country='england',
  postcode='ng321re', town_or_city='testcity', street_address1='1 test street', county='sussextest', date='2019-01-01')
  order.save()
  self.assertEqual(order.full_name, "mr Test")
  self.assertEqual(order.county, 'sussextest')
  

   