from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from image_cropping import ImageRatioField

# Blog models
class Post(models.Model):
    STATUS_CHOICE = (
        ('draft','Wstrzymaj'),
        ('published', 'Opublikuj')
    )
    title = models.TextField(null=False, verbose_name="Tytuł")
    subtitle = models.TextField(null=True, blank=True, verbose_name="Podtytuł(Opcjonalnie)")
    text = models.TextField(verbose_name="Treść Posta")
    image = models.ImageField(upload_to ='uploads/articles/thumbnails', null=False, verbose_name="Zdjęcie")
    #post_thumbnail = ImageRatioField('thumbnail', '1120x400', size_warning=True, verbose_name="Miniaturka 1120x400")
    slug = models.SlugField(max_length=250, unique=True, null=False)
    hits = models.IntegerField(default=0, editable=False, verbose_name="Wyświetlenia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data aktualizacji")

    class Meta:
        ordering = ['-created_at', 'updated_at']
        verbose_name = "Post"
        verbose_name_plural = "Posty"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('website:post', args=[self.slug])

