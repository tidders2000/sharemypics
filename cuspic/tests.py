from django.test import TestCase
from .models import CusPic

# Create your tests here.
class CusPicTests(TestCase):
    """
    tests to run against CusPic models
    
    """

    
    def test_adding_a_pic(self):
        test_pic = CusPic(event_name='LeMan', uploader_id='3', price=2.99, info='here is some info',image='test.jpg')
        test_pic.save
        self.assertEqual(test_pic.event_name,'LeMan')
        self.assertEqual(test_pic.uploader_id,'3')
        self.assertEqual(test_pic.price,2.99)
        self.assertEqual(test_pic.info,'here is some info')
        self.assertEqual(test_pic.image,'test.jpg')
    
  