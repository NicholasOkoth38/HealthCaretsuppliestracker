from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('login')

        self.user_data={
            'email':'email@gmail.com',
            'name':'email',
            'password':'123456789',
            'phone_number':'123456789',
            'location':'gelegele',
        }

        return super().setUp()
    
    def tearDown(self):

        return super().tearDown()