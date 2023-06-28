from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .models import Vacancy
from .forms import ContactForm, ParsingForm
from django.core.mail import send_mail

from django.views.generic import ListView
from django.views.generic.edit import FormView


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


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'hhapp/index.html'
    context_object_name = 'vacancys'


class ContactFormView(FormView):
    template_name = 'hhapp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('hh:home')

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ParsingFormView(FormView):
    template_name = 'hhapp/parsing.html'
    form_class = ParsingForm
    success_url = reverse_lazy('hh:home')

    def form_valid(self, form):
        form.parsing()
        return super().form_valid(form)
