from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from core import libutils
from core.models import *

import json


def cadwriter(request):
    if request.method == 'POST':
        writer = Writer()
        writer.init_from_request(request)
        writer.save()
        return redirect('/loginpage')
    return render(request, 'cad_page.html')
    
def writerlogout(request):
    logout(request)
    return redirect('/')

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

@login_required
def postsave(request):
    if request.method == 'POST':
        post = PostWritten()
        post.init_from_request(request)
        post.save()
        return HttpResponse('Sucesso ao salvar!')
    return HttpResponse('')

def postfeed(request):
    # writter = Writer.objects.get(user=get_user(request))
    postagens = PostWritten.objects.all()
    return render(request, 'feed_page.html', {'posts': postagens})


def index(request):
    return render(request, 'index.html')