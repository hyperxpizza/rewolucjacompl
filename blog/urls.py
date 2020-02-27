from django.conf.urls import url
from . import views
from django.urls import path 
app_name='blog'

urlpatterns = [
    path('', views.all_posts, name="all_posts"),
    path('<int:id>/', views.post_detail, name='post_detail')
]