from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    #index
    path('', views.index, name='index')
]