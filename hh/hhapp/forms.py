from django import forms
import requests
from django.core.mail import send_mail

from .models import City, Currency, Vacancy


class ContactForm(forms.Form):
    firstname = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    text = forms.CharField(label='Ваш комментарий')

    def send_mail(self):
        send_mail(
            self.cleaned_data['firstname'],
            self.cleaned_data['email'],
            self.cleaned_data['text'],
            ["to@example.com"],
            fail_silently=True,
        )


class ParsingForm(forms.Form):
    search = forms.CharField(label='Ключевое слово')
    per_page = forms.CharField(label='Число вакансий')

    def parsing(self):
        search = self.cleaned_data['search']
        url = 'https://api.hh.ru/vacancies'
        params = {'page': 1,
                  'per_page': self.cleaned_data['per_page'],
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