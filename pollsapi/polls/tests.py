from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from polls import apiviews
# Create your tests here.


class TestPoll(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = apiviews.PollList.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client = APIClient()
    
    @staticmethod
    def setup_user():
        user = get_user_model()
        return user.objects.create_user(
            'test',
            email='testuser@maildomain.net',
            password='abc@123'
        )
        
    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.view(request)
        print(response)
        self.assertEqual(
            response.status_code, 200, 
            'Expected Response Code 200, received {0} instead'.format(response.status_code)
            )
    
    def test_list2(self):
        self.client.login(username='test', password='abc@123')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead'.format(response.status_code))
        