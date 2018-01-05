from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json


def postingcms(request):
    if request.method == 'POST':
        jsonpost = request.POST
        print(json.dumps(jsonpost))
        return HttpResponse(json.dumps(jsonpost))
    return HttpResponse('consultado via get')


def index(request):
    return render(request, 'index.html')