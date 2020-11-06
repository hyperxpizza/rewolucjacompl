from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Subscriber, Newsletter, ProductOptions, ProductImage, Product, Order, OrderItem

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

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','city', 'country','paid','sent','created_at','updated_at']
    list_filter = ['paid','created_at','updated_at', 'sent']
    inlines = [OrderItemInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Order, OrderAdmin)