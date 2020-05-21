from django.shortcuts import render

# Create your views here.

def index(request):
        return render(request, 'core/index.html')

def kodea_eskuratu(request):
        return render(request, 'core/form_kodea_eskuratu.html')

def aurrebaldintzak(request):
        return render(request, 'core/aurrebaldintzak.html')

def download(request):
        if "google_opt" in request.POST:
                return render(request, 'core/google_download.html')
        else:
                return render(request, 'core/download.html')