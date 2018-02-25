from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from core import libutils
from core.models import *

import json


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
    return render(request, 'error_login.html')


def loginpage(request):
    return render(request, 'login_page.html')

def postwrite(request):
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