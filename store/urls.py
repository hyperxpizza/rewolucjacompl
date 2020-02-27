from django.conf.urls import url
from . import views

app_name='store'

urlpatterns =[
    url(r'^$', views.all_products, name='all_products'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category_detail, name='category_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
