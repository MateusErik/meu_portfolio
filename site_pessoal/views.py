from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def projetos(request):
    return render(request, "projetos.html")

def contatos(request):
    return render(request, "contatos.html")

def sobre(request):
    return render(request, "sobre.html")
