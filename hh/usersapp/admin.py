from django.contrib import admin
from .models import HhUser
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(HhUser)
TokenAdmin.raw_id_fields = ['user']