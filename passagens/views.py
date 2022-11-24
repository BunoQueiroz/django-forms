from django.shortcuts import render, redirect
from .forms import PassagensForms

def home(request):
    form = PassagensForms
    context = {'form':form}

    return render(request, 'index.html', context)

def consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        if form.is_valid():
            context = {'form': form}
            return render(request, 'consulta.html', context)
        return render(request, 'index.html', {'form':form})
