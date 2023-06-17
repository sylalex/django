from django.contrib import admin
from .models import Vacancy, City, Currency

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(City)
admin.site.register(Currency)
