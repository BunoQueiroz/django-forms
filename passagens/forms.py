from django import forms
from tempus_dominus.widgets import DatePicker

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=50, strip=True, required=True)
    destino = forms.CharField(label='Destino', max_length=50, strip=True, required=True)
    data_ida = forms.DateField(label='Data de ida', required=True, widget=DatePicker())
    data_volta = forms.DateField(label='Data de volta', required=True, widget=DatePicker())
