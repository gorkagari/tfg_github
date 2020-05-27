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

def google_aurrebaldintzak(request):
        return render(request, 'core/google_aurrebaldintzak.html')

def twitter_aurrebaldintzak(request):
        return render(request, 'core/twitter_aurrebaldintzak.html')

def github_aurrebaldintzak(request):
        return render(request, 'core/github_aurrebaldintzak.html')


def download(request):
        # ONLY GOOGLE HAS BEEN CHOSEN
        if ("google_opt" in request.POST) and not("twitter_opt" in request.POST) and not("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/google_auth.txt')
                filename = "google_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # ONLY TWITTER HAS BEEN CHOSEN
        elif not("google_opt" in request.POST) and ("twitter_opt" in request.POST) and not("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/twitter_auth.txt')
                filename = "twitter_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # ONLY GITHUB HAS BEEN CHOSEN
        elif not("google_opt" in request.POST) and not("twitter_opt" in request.POST) and ("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/github_auth.txt')
                filename = "github_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # GOOGLE AND TWITTER HAVE BEEN CHOSEN
        elif ("google_opt" in request.POST) and ("twitter_opt" in request.POST) and not("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/google_twitter_auth.txt')
                filename = "google_twitter_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # GOOGLE AND GITHUB HAVE BEEN CHOSEN
        elif ("google_opt" in request.POST) and not("twitter_opt" in request.POST) and ("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/google_github_auth.txt')
                filename = "google_github_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # TWITTER AND GITHUB HAVE BEEN CHOSEN
        elif not("google_opt" in request.POST) and ("twitter_opt" in request.POST) and ("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/twitter_github_auth.txt')
                filename = "twitter_github_auth.txt"
                content = r.text
                response = HttpResponse(content, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
        # GOOGLE, TWITTER AND GITHUB HAVE BEEN CHOSEN
        elif ("google_opt" in request.POST) and ("twitter_opt" in request.POST) and ("github_opt" in request.POST):
                r = requests.get(
                        'https://raw.githubusercontent.com/gorkagari/tfg_github/master/google_twitter_github_auth.txt')
                filename = "google_twitter_github_auth.txt"
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