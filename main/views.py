from django.shortcuts import render, redirect
from .models import lista

def Home(req):
    data = {}
    trabalhador = lista.objects.all()
    data['trabalhador'] = trabalhador
    return render(req, "index.html", data)



def actualizar(req,id):
    funcionario = lista.objects.get(id=id)
    return render(req, "update.html", {'funcionario':funcionario})

def editar(req):

    a = req.POST['Nome']
    b = req.POST['idade']
    c = req.POST['profissao']

    funcionario = lista.objects.get(id=req.POST['id'])

    funcionario.Nome=a
    funcionario.idade=b
    funcionario.profissao=c

    funcionario.save()
    return redirect('/')


def adcionar(req):
    data = req.POST
    funcionarionovo = lista.objects.create(
        Nome = data['Nome'],
        idade = data['idade'],
        profissao = data['profissao'],

    )
    funcionarionovo.save()
    req.session['pk'] = funcionarionovo.pk
    return redirect('/')
    

def deleta(req, id):
    funcionario = lista.objects.get(id=id)
    funcionario.delete()
    return redirect('/')


def add(req):
    return render(req, "add.html")