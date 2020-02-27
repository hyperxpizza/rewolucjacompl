from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','adress','postal_code','city','paid','sent','created_at','updated_at']
    list_filter = ['paid','created_at','updated_at']
    inlines = [OrderItemInLine]

admin.site.register(Order,OrderAdmin)