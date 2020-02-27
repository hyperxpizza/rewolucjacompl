from django.conf.urls import url
from django.urls import path
from . import views

app_name='pages'

urlpatterns =[
    path('art', views.art, name='art'),
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.contact_success, name='contact_success'),
    path('contact_mail/', views.contact_mail, name='contact_mail'),
    path('', views.about, name='about')
]