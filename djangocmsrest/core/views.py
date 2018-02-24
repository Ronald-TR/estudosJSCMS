from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from core.models import *
import json
from core import libutils

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