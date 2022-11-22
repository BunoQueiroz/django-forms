from django import forms

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=50, strip=True, required=True)
    destino = forms.CharField(label='Destino', max_length=50, strip=True, required=True)
    data_ida = forms.DateField(label='Data de ida', required=True)
    data_volta = forms.DateField(label='Data de volta', required=True)
