from django.contrib import admin
from .models import ArtImage, IndexSliderImage

class ArtImageAdmin(admin.ModelAdmin):
    list_display=['name','uploaded_at']

admin.site.register(ArtImage, ArtImageAdmin)

class IndexSliderImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'uploaded_at']

admin.site.register(IndexSliderImage, IndexSliderImageAdmin)

