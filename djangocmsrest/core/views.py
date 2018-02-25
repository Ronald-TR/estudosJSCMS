from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from core import libutils
from core.models import *

import json


def cadwriter(request):
    return render(request, 'cad_page.html')


def writerlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    writeruser = authenticate(request, username=username, password=password)

    if writeruser is not None:
        login(request, writeruser)
        return redirect('/postwrite')
    else:
        return redirect('/errorlogin')

def errorlogin(request):
    error = {
        'errormsg': 'Erro ao autenticar',
        'errordetail': 'Por favor... retorne ao inicio e tente novamente'
    }
    return render(request, 'error_page.html', error)


def loginpage(request):
    return render(request, 'login_page.html')


def postwrite(request):
    user  = get_user(request)
    error = {
        'errormsg': 'Desculpe, anônimo',
        'errordetail': 'Usuarios anonimos "ainda"  não podem escrever, logue-se ou cadastre-se'
    }
    if type(user) is AnonymousUser:
        return render(request, 'error_page.html', error)
    return render(request, 'post_write_page.html')

def postlist(request):
    if request.method == 'POST':
        postagem = libutils.safeSerialization(Postagem, request.POST)
        message = 'sucesso ao salvar'
        try:
            postagem.save()
        except Exception as e:
            message = e    
        return HttpResponse(message)
    postcount = json.dumps({'postcount': Postagem.objects.all().count()})
    return HttpResponse(postcount)


def index(request):
    return render(request, 'index.html')