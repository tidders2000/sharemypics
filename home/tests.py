from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    
    """
    tests to run against home
    
    """
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_search(self):
     page = self.client.get("/cuspic/search/?q=Le+Man+2019")
     self.assertEqual(page.status_code, 200)