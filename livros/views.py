from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

app_name='livros'

def lista_livros(request):
    livro=Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livro':livro})


def ver_livro(request, id):
    livro=Livro.objects.get(id=id)
    return render(request, 'livros/ver_livro.html', {'livro':livro})


def cadastrar_livros(request):
    form= LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request, 'livros/cadastrar_livros.html', {'form':form})


def editar_livros(request, id):
    livro=Livro.objects.get(id=id)
    form=LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request, 'livros/editar_livros.html', {'form':form})
