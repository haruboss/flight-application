from django import forms
from .models import *


class FlightCreateForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        # widgets = {
        #     'ordered_by': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Your Name '
        #     }),
        #     'shipping_address': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Your Address'
        #     }),
        #     'mobile': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Phone Number'
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Email Id',
        #     })
        # }
