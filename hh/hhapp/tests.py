from hh.wsgi import *
import requests
from django.test import TestCase, Client
from .models import Vacancy, City, Currency
from usersapp.models import HhUser


# Create your tests here.
class DbTestCase(TestCase):
    def setUp(self):
        City.objects.get_or_create(name='Москва')
        city_values = City.objects.filter(name='Москва').first().id
        Currency.objects.get_or_create(name='Rub')
        currency_values = Currency.objects.filter(name='Rub').first().id
        Vacancy.objects.create(name='Python', city_id=city_values, currency_id=currency_values)

    def test_vacancy(self):
        self.assertTrue(Vacancy.objects.get(name='Python'))


class WebTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class UserTestCase(TestCase):
    def setUp(self):
        HhUser.objects.create_user('admin2', password='admin2', email='test@test.ru')
        self.client = Client()

    def test_status(self):
        # response = self.client.get('/users/login/')
        # self.assertEqual(response.status_code, 200)

        response = self.client.login(username='admin2', password='admin2')
        self.assertTrue(response)


class TokenTestCase(TestCase):
    def test_status(self):
        url = 'http://127.0.0.1:8000/api/vacancies/'

        r = requests.get(url, headers={
            'Authorization': 'Token 48b15421ff68ebc5df66186a2ec530593545017b'
        }
                         )
        self.assertEqual(r.status_code, 200)
