from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .choices import tipos_classe
from .validation import *

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

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        campo_tem_numero(origem, 'origem', lista_erros)
        campo_tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        if lista_erros is not None:
            print(lista_erros)
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
