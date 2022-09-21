from django.contrib import admin

from .models import *
# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name','category','is_active')


@admin.register(Product_Inventry)
class ProductInventryAdmin(admin.ModelAdmin):
    list_display = ('product', 'price','sell','discount')
    readonly_fields = ('discount',)

@admin.register(Product_Stock)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock')

admin.site.register(Category)
admin.site.register(Brand)