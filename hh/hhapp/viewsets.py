from rest_framework.permissions import IsAdminUser
from .models import Vacancy, City, Currency
from .permissions import ReadOnly
from .serializers import VacancySerializer, CitySerializer, CurrencySerializer
from rest_framework import viewsets


class VacancyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
