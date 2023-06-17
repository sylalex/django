from django.core.management.base import BaseCommand
from hhapp.models import Vacancy, City, Currency
import requests
import pprint


class Command(BaseCommand):

    def handle(self, *args, **options):
        search = 'ml'
        url = 'https://api.hh.ru/vacancies'
        params = {'page': 1,
                  'per_page': 20,
                  'text': search,
                  'area': 113,
                  'only_with_salary': True}
        response = requests.get(url, params=params)
        print(f'Статус ({search}): {response.status_code}')
        result = response.json()
        # pprint.pprint(result)
        list_vac = result['items']
        for i in range(len(list_vac)):

            City.objects.get_or_create(name=list_vac[i]['area']['name'])
            city_values = City.objects.filter(name=list_vac[i]['area']['name']).first().id
            # print(city_values)
            # print(type(city_values))
            Currency.objects.get_or_create(name=list_vac[i]['salary']['currency'])
            currency_values = Currency.objects.filter(name=list_vac[i]['salary']['currency']).first().id
            Vacancy.objects.create(name=list_vac[i]['name'], salary_from=list_vac[i]['salary']['from'],
                                   salary_to=list_vac[i]['salary']['to'], city_id=city_values,
                                   currency_id=currency_values)
