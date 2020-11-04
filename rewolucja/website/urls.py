from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    #index
    path('', views.index, name='index'),
    #post_detail
    path('/blog/<slug:slug>/', views.post_detail, name="post_detail"),
    #store
    path('/sklep', views.store, name="store"),
    #product detail
    path('/sklep/<slug:slug>/', views.product_detail, name="product_detail"),
    #art
    path('/sztuka', views.art, name="art"),
    #search by tag
    path('tag/<slug:slug>', views.view_by_tag, name="view_by_tag")

]