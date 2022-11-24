from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .choices import tipos_classe

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=50, strip=True, required=True)
    destino = forms.CharField(label='Destino', max_length=50, strip=True, required=True)
    data_ida = forms.DateField(label='Data de ida', required=True, widget=DatePicker(), initial=datetime.today)
    data_volta = forms.DateField(label='Data de volta', required=True, widget=DatePicker(), initial=datetime.today)
    data_pesquisa = forms.DateField(label='Data da pesquisa', required=True, disabled=True, initial=datetime.today)
    detalhes = forms.CharField(
        label='Informações extras',
        widget=forms.Textarea(),
        required=False,
        max_length=200
    )
    classe = forms.ChoiceField(choices=tipos_classe, initial='1')
    email = forms.EmailField(max_length=100, required=True)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Esse campo não aceita números')
        else:
            return origem