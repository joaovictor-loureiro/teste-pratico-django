from django.shortcuts import render, redirect
from app.forms import PessoaForm
from app.models import Pessoa

from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Pessoa.objects.filter(nome__icontains=search)
    else:
        data['db'] = Pessoa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    html = requests.get("https://gerador-nomes.herokuapp.com/nome/aleatorio").content
    soup = BeautifulSoup(html, 'html.parser')

    soup = soup.text
    soup = soup.replace('"', '')
    soup = soup.replace('[', '')
    soup = soup.replace(']', '')

    aleatorio = []
    aleatorio = soup.split(',')

    nome_aleatorio = aleatorio[0]
    sobrenome_aleatorio = aleatorio[1] + " " + aleatorio[2]

    data = {}

    data['nome_aleatorio'] = nome_aleatorio
    data['sobrenome_aleatorio'] = sobrenome_aleatorio

    data['form'] = PessoaForm(initial={'nome':nome_aleatorio, 'sobrenome':sobrenome_aleatorio})

    return render(request, 'form.html', data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')