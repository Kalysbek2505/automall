from django import forms
from .models import Appointment, Contact

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'service', 'date']


class ContactForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=15)
    phone_number = forms.CharField(label='Номер телефона', max_length=15)

