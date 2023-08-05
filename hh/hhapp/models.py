from contextlib import nullcontext

from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=256)
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING)
    salary_from = models.IntegerField(blank=True, null=True)
    salary_to = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class City(Name):
    pass
    # name = models.CharField(max_length=256, unique=True)

    # def __str__(self):
    #     return self.name


class Currency(Name):
    pass
    # name = models.CharField(max_length=256, unique=True)
    #
    # def __str__(self):
    #     return self.name
