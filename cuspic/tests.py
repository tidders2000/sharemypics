from django.test import TestCase
from .models import CusPic
from django.test import TestCase, Client
from django.contrib.auth.models import User
csrf_client = Client(enforce_csrf_checks=True)

# Create your tests here.
class CusPicTests(TestCase):
    """
    tests to run against CusPic models
    
    """

    
    def test_adding_a_pic(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        test_pic = CusPic(event_name='LeMan', user=self.user, price=2.99, info='here is some info',image='test.jpg')
        test_pic.save
        self.assertEqual(test_pic.event_name,'LeMan')
        self.assertEqual(test_pic.user,self.user)
        self.assertEqual(test_pic.price,2.99)
        self.assertEqual(test_pic.info,'here is some info')
        self.assertEqual(test_pic.image,'test.jpg')
    
    def test_my_images(self):
       c = Client()
       c.login(username='fred', password='secret', email='test@test.com')
       page = self.client.get("/cuspic/my_images",follow=True)
       self.assertEqual(page.status_code, 200)
       
    
    def test_search(self):
       
       page = self.client.get("/cuspic/search?q=Le+Man+2019",follow=True)
       self.assertEqual(page.status_code, 200)