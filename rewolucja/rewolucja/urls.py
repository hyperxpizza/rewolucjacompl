from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

sitemaps = {}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]
