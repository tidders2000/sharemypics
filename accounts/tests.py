from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):
    
    """
    tests to run against home
    
    """
    def test_logon_index(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_registration_view_logedin_redirect(self):
        page = self.client.get("/accounts/register")
        self.assertEqual(page.status_code, 301)
    
    def test_logon_profile(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345', email='test@test.com')
        page = c.get("/profile")
        self.assertEqual(page.status_code, 200)
        
    