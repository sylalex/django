from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Vacancy
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    vacancys = Vacancy.objects.all()
    return render(request, 'hhapp/index.html', context={'vacancys': vacancys})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            send_mail(
                firstname,
                text,
                email,
                ["to@example.com"],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    return render(request, 'hhapp/contact.html', {'form': form})
