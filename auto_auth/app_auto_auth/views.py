from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
import requests
from os import getcwd

# Create your views here.

def index(request):
        return render(request, 'core/index.html')

def kodea_eskuratu(request):
        return render(request, 'core/form_kodea_eskuratu.html')

def aurrebaldintzak(request):
        return render(request, 'core/aurrebaldintzak.html')

def download(request):
        if "google_opt" in request.POST:
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/google_auth.txt')
                filename = "google_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
       
        else:
                r = requests.get('https://raw.githubusercontent.com/gorkagari/tfg_github/master/auth.txt')
                filename = "auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response