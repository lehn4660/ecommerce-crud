from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('seller:index')
        res = self.client.get(url)
        print(res.data)
        self.assertEquals(res.data,'Congratulations...you have created an API')

    def test_number(self):
        url = reverse('seller:number')
        res = self.client.get(url)
        self.assertEqual(res.data,10)


