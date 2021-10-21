from django.urls import reverse
from rest_framework import response, status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class UserTest(APITestCase):


    def can_create_user(self):
        url = reverse('users-list')
        data = {
            'email': 'Test@gmail.com',
            'name': 'Test',
            'city': 'Test',
            'state': 'Test',
            'zipcode': 'Test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().name, 'Test')


    def can_get_user(self):
        user = User.objects.get()
        url = reverse('users-list',kwargs={'User':user.email})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)


    def can_delete_user(self):
        user = User.objects.get()
        url = reverse('users-list',kwargs={'User':user.email})
        response = self.client.delete(url, format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def can_update_user(self):
        user = User.objects.get()
        url = reverse('users-list',kwargs={'User':user.email})
        new_data = {
            'email': 'newTest@gmail.com',
            'name': 'newTest',
            'city': 'newTest',
            'state': 'newTest',
            'zipcode': 'newTest'
        }
        response = self.client.put(url,new_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
