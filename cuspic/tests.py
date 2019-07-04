from django.test import TestCase
from .models import CusPic

# Create your tests here.
class CusPicTests(TestCase):
    """
    tests to run against CusPic models
    
    """
    def test_str(self):
        test_event = CusPic(event_name='LeMan')
        self.assertEqual(str(test_event),'LeMan')
    
    def test_str_id(self):
        test_id = CusPic(uploader_id='3')
        self.assertEqual(str(test_id),'3')
    
  