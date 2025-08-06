from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')     
    search_fields = ('name',)            
    list_filter = ('price',)      

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity')
    list_filter = ('menu_item',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username',)
    filter_horizontal = ('items',)  # Better interface for ManyToManyField
    date_hierarchy = 'created_at'      