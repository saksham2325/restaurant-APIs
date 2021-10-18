# from django.http import response
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from django.urls import reverse

# When I run the command python manage.py test 3 errors are there.

class UserTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {'name' : 'Go to Ibiza'}
        self.response = self.client.post(reverse('user-list'), self.user_data, format = "json")

    def test_api_can_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_user(self):
        user=User.objects.get()
        response=self.client.get(reverse('pk', kwargs = {'user': user.id}), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)
    
    def test_api_can_update_user(self):
        user=User.objects.get()
        change_user = {'name' : 'something new'}
        res = self.client.put(reverse('details', kwargs={'User': user.id}), change_user, format= "json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_api_can_delete_user(self):
        user=User.objects.get()
        response = self.client.delete(reverse('details',kwargs={'pk': user.id}),format = "json", follow=True)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)