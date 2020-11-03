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
    tags = TaggableManager(verbose_name="tagi")
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

#art model
class ArtItem(models.Model):
    title = models.TextField(null=False, verbose_name="Tytuł")
    description = models.TextField(null=True, blank=True, verbose_name="Opis(Opcjonalnie")
    author = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/art/images', null=False, verbose_name="Zdjęcie")
    visible = models.BooleanField(default=True, verbose_name="Wyświetlaj")
    tags = TaggableManager(verbose_name="tagi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data aktualizacji")

    class Meta:
        ordering = ['-created_at', 'updated_at']
        verbose_name = "Sztuka"
        verbose_name_plural = "Sztuka"

    def __str__(self):
        return self.title


# Store models
class ProductCategory(models.Model):
    name = models.TextField(blank=True, null=False, verbose_name="Nazwa Kategorii/Kolekcji")
    description = models.TextField(blank=True, null=True, verbose_name="Opis(Opcjonalnie)")
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data aktualizacji")

    class Meta:
        ordering = ('name', 'created_at')
        verbose_name = "Kategoria Produktu"
        verbose_name_plural = "Kategorie Produktów"

    def  __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='category', on_delete=models.PROTECT, verbose_name="Kategoria")
    name = models.TextField(blank=True, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=False, verbose_name="Opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    available = models.BooleanField(default=True, verbose_name="Dostępność")
    stock = models.PositiveIntegerField(verbose_name="Ilość")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data aktualizacji")

    class Meta:
        ordering = ('created_at')
        verbose_name="Produkt"
        verbose_name_plural="Produkty"

    def __str__(self):
        return self.name
    
    def check_if_sold_out(self):
        if self.stock == 0:
            self.available = False

    def get_absolute_url(self):
        return reverse('website:product_detail', args=[self.slug])

class ProductOptions(models.Model):
   SIZE_OPTIONS = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("NO SIZE", "Brak rozmiaru"),
        ("universal", "Uniwersalny")
    )

    product_size = models.CharField(max_length=30, choices=SIZE_OPTIONS, verbose_name="Rozmiar produktu")
    stock = models.PositiveIntegerField()
    sold_out = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Opcje produktu"
        verbose_name_plural = "Opcje produktów"

    def check_if_sold_out(self):
        if self.stock == 0:
            self.sold_out = True
            
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField()