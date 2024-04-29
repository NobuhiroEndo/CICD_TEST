from django.test import TestCase
from django.urls import reverse, resolve
from .views import *
# Create your tests here.

class TestsUrls(TestCase):
    def test_index_url(self):
        url = reverse('CICD:test')
        self.assertEqual(resolve(url).func, index)