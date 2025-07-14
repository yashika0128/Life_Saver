from django import forms
from .models import Donor, Receiver

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = '__all__'
