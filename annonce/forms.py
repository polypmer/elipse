from functools import partial
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Pret, Donne, Exchice
from django.contrib.auth.models import

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DonneForm(forms.ModelForm):
    
    class Meta:
        model = Donne
        fields = ['title', 'description', 'myzip', 'location', 'picture', 'quality', 'mytype']  
