from django import forms
from.models import Driver,Vehicle

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'        