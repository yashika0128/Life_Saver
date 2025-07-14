from django import forms
from .models import Donor, Receiver

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = '__all__'
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'required_blood_group': forms.Select(attrs={'class': 'form-select'}),
            'urgency': forms.Select(attrs={'class': 'form-select'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control'}),
        }