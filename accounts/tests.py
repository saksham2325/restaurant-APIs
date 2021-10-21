from django.urls import reverse
from rest_framework import response, status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class UserTest(APITestCase):


    def setUp(self):
        url = reverse('user-list')
        data = {
            'email': 'Test1@gmail.com',
            'name': 'Test1',
            'city': 'Test1',
            'state': 'Test1',
            'zipcode': 'Test1',
            'phone': '1234',
            'password': '1234'
        }
        client = APIClient()
        response = client.post(url, data, format='json')

    def test_can_create_user(self):
        url = reverse('user-list')
        data = {
            'email': 'Test@gmail.com',
            'name': 'Test',
            'city': 'Test',
            'state': 'Test',
            'zipcode': 'Test',
            'phone': '1234',
            'password': '1234'
        }

        client = APIClient()
        response = client.post(url, data, format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_can_get_user(self):

        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        client = APIClient()
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_can_delete_user(self):
        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        response = self.client.delete(url, format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_update_user(self):
        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        new_data = {
            'email': 'newTest@gmail.com',
            'name': 'newTest',
            'city': 'newTest',
            'state': 'newTest',
            'zipcode': 'newTest',
            'phone': '1234',
            'password': '1234'
        }
        response = self.client.put(url,new_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
