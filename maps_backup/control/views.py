from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,"main.html")  

def cadastroAtivos(request):
    return render(request,"cadastros/ativos.html")

def cadastroemissores(request):
    return render(request,"cadastros/emissores.html")

def agentescustodia(request):
    return render(request,"cadastros/agentesdecustodia.html")

def cadastroadministradores(request):
    return render(request,"cadastros/administradores.html")


def cadastrosinvestidores(request):
    return render(request,"cadastros/investidores.html")
