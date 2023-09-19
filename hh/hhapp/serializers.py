from .models import Vacancy, City, Currency
from rest_framework import serializers


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        # read_only=True,
        queryset=City.objects.all(),
        view_name='city-detail',
    )
    currency = serializers.HyperlinkedRelatedField(
        # read_only=True,
        queryset=Currency.objects.all(),
        view_name='currency-detail',
    )

    class Meta:
        model = Vacancy
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class CurrencySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'

