from django.shortcuts import render, redirect
from .forms import PassagensForms

def home(request):
    form = PassagensForms
    context = {'form':form}

    return render(request, 'index.html', context)

def consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        context = {'form': form}
        return render(request, 'consulta.html', context)
    return redirect('home')
