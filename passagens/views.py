from django.shortcuts import render, redirect
from .forms import PassagensForms, PessoaForms

def home(request):
    form = PassagensForms
    pessoa = PessoaForms
    context = {'form':form, 'pessoa':pessoa}

    return render(request, 'index.html', context)

def consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        pessoa = PessoaForms(request.POST)
        if form.is_valid():
            context = {'form': form, 'pessoa': pessoa}
            return render(request, 'consulta.html', context)
        return render(request, 'index.html', {'form':form, 'pessoa':pessoa})
