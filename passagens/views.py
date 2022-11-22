from django.shortcuts import render
from .forms import PassagensForms

def home(request):
    form = PassagensForms
    context = {'form':form}

    return render(request, 'index.html', context)
