from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from core.models import *
import json


def postingcms(request):
    if request.method == 'POST':
        postagem = Postagem()
        if postagem.safeSerialization(request.POST):
            message = 'sucesso'
            try:
                postagem.save()
            except Exception as e:
                message = e    
            return HttpResponse(message)
    return HttpResponse('consultado via get')


def index(request):
    return render(request, 'index.html')