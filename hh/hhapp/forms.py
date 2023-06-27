from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    text = forms.CharField(label='Ваш комментарий')
