from django.contrib import admin
from .models import Category, Product, Images, Review

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}


class ImageInline(admin.StackedInline):
    model = Images
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')
    list_editable = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        ImageInline
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')