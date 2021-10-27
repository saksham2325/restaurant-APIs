from ddf import G
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from accounts.serializers import UserSerializer


class UserTest(APITestCase):
    # user = G(User)
    # print(user.email)
    def setUp(self):
        user = User.objects.create_user('test1@gmail.com', '1234',name='Test1',city='Test1',state='Test1',zipcode='Test1',phone='1234567890')

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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data,expected_data)

    def test_can_get_user(self):

        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        client = APIClient()
        user = User.objects.get(pk=user.id)
        serializer = UserSerializer(user)
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_can_delete_user(self):
        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        client = APIClient()
        response = self.client.delete(url, format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_update_user(self):
        user = User.objects.get()
        url = reverse('user-detail',kwargs={'pk':user.id})
        new_data = {
            'email': 'newemail@gmail.com',
            'name': 'newTest',
            'city': 'newTest',
            'state': 'newTest',
            'zipcode': 'newTest',
            'phone': '1234',
            'password': '1234',
            'balance': '1000'
        }
        client = APIClient()
        response = self.client.put(url,new_data,format='json')
        user = User.objects.get(pk=user.id)
        serializer = UserSerializer(user)
        print(serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
