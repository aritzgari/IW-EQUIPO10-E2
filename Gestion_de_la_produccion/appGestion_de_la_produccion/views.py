from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("Esta es la primera pagina de aqui directos a la entrega")



# Create your views here.
