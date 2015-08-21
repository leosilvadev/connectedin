# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {"perfil": perfil})

def convidar(request, perfil_id):
    perfil = Perfil.convidar(request, Perfil.objects.get(id=perfil_id))
    return render(request, 'index.html', {"perfis": Perfil.objects.all()})
