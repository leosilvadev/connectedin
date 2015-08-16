# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Leonardo', 'leosilvadev@gmail.com', '2312312312', 'GSW')

    return render(request, 'perfil.html', {"perfil": perfil})
