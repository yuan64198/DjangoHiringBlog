from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class BlogTestCase(TestCase):
    def setUp(self):
        pass
        #User.objects.create(username = 'test', email = 'test@gmail.com', password = 'Test123456')