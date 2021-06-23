from django.shortcuts import render
from .models import Teste

# Create your views here.

def home(request):
    return render(request, 'home.html')


def nomes(request):
    nome=Teste.objects.all()
    return render(request, 'nomes.html', {'nome':nome})
