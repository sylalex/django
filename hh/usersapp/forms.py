from django.contrib.auth.forms import UserCreationForm
from .models import HhUser


class RegForm(UserCreationForm):
    class Meta:
        model = HhUser
        fields = ('username', 'email', 'password1', 'password2')
