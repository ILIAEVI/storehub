from django.contrib import admin
from store.models import Product, Category
from store.views import get_products_for_category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    list_filter = ('categories',)
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',)
    readonly_fields = ('quantity',)
