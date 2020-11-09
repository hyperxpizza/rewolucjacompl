from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Product

class Static_Sitemap(Sitemap):
    changefreq = 'hourly'
    priority = '1'

    def items(self):
        return [
            'website:index',
            'website:art',
            'website:store'
        ]

    def location(self, item):
        return reverse(item)

class Post_Sitemap(Sitemap):
    changefreq = 'hourly'
    priority ='0.8'

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at


class Product_Sitemap(Sitemap):
    changefreq = 'hourly'
    priority ='0.5'

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated_at