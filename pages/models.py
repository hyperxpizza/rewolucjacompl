from django.db import models

class ArtImage(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='art/%Y/%m/%d', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    author = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ('name',)
        verbose_name = 'Art Image'
        verbose_name_plural = 'Art Images'

class IndexSliderImage(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='aboutslider/%Y/%m/%d', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Index Slider Image'
        verbose_name_plural = 'Index Slider Images'
