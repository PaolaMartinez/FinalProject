from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient', views.patient, name='patient'),
    path('trial', views.trial, name='trial'),
    path('channel', views.channel, name='channel')
]