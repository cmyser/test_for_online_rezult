from django.contrib import admin

from .models import Product, Product_Info, Mentions


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ['title']


@admin.register(Product_Info)
class Product_InfoAdmin(admin.ModelAdmin):
    list_filter = ('product',)
    search_fields = ['country']


@admin.register(Mentions)
class MentionsAdmin(admin.ModelAdmin):
    list_filter = ('product',)
    search_fields = ['product']
    
