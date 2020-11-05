from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Subscriber, Newsletter, ProductOptions, ProductImage, Product

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Wyślij newsletter do subskrybentów"

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('text',)
    prepopulated_fields = {'slug': ('title',)}

class ProductOptionInline(admin.TabularInline):
    model = ProductOptions
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductOptionInline, ProductImageInline]

class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]


admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)