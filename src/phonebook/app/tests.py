import json
from django.contrib.auth.models import User
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from .models import Phonebook


class PhonebookTest(APITestCase):
    client=APIClient()

    def test_post(self):
        data = {
            "id": 1,
            "lastname": "Ishola",
            "firstname": "Sodiq",
            "phone_number": "0816604",
            "email": "olatundesodiq@gmail.com",
            "address": "No 5, Lekki area"
        }
        url = '/api/phonebook/'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['lastname'], 'Ishola')

class GetPhonebook(APITestCase):
    def setUp(self):
        self.data = Phonebook.objects.create(
            id = 1,
            lastname = "Ishola",
            firstname = "Sodiq",
            phone_number = "0816604",
            email = "olatundesodiq@gmail.com",
            address = "No 5, Lekki area"                                                                                                                                                                
        )       

    def test_get_all(self):
        url = '/api/phonebook/'
        # print(url)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_phonebook(self):
        url = '/api/phonebook/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_unable_get_unavailable_phonebook(self):
        url = '/api/phonebook/11/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_a_phonebook(self):
        data = {
            "lastname": "ola",
            "firstname": "ade",
            "phone_number": "0816603244",
            "email": "olatund@gmail.com",
            "address": "No 5, Lekki lagos"
        }
        url = '/api/phonebook/1/'
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lastname'], 'ola')
        print(response.data)

    def test_delete_a_phonebook(self):
        url = '/api/phonebook/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
