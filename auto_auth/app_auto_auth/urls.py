from . import views
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('',views.index, name='index'),
    path('kodea_eskuratu',views.kodea_eskuratu, name='kodea_eskuratu'),
    path('aurrebaldintzak',views.aurrebaldintzak, name='aurrebaldintzak'),
    path('download',views.download, name='download'),
    ]