from django.contrib import admin

from .models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'category', 'authors', 'price', 'amount')
    list_display = ('title',)
    list_filter = ('price', )
    search_fields = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    search_fields = ('name', )
