
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)

class QuoteForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    service_type = forms.ChoiceField(choices=[
        ('heating_installation', 'Установка системы отопления'),
        ('maintenance', 'Техническое обслуживание'),
        ('repair', 'Ремонтные работы'),
        ('consultation', 'Консультация')
    ])
    details = forms.CharField(widget=forms.Textarea)
