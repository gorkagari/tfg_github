from . import views
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('',views.index, name='index'),
    path('kodea_eskuratu',views.kodea_eskuratu, name='kodea_eskuratu'),
    path('aurrebaldintzak',views.aurrebaldintzak, name='aurrebaldintzak'),
    path('google_aurrebaldintzak',views.google_aurrebaldintzak, name='google_aurrebaldintzak'),
    path('twitter_aurrebaldintzak',views.twitter_aurrebaldintzak, name='twitter_aurrebaldintzak'),
    path('github_aurrebaldintzak',views.github_aurrebaldintzak, name='github_aurrebaldintzak'),
    path('download',views.download, name='download'),
    ]