from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from website.sitemaps import Static_Sitemap, Post_Sitemap, Product_Sitemap

sitemaps = {
    'static': Static_Sitemap(),
    'post': Post_Sitemap(),
    'product': Product_Sitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)