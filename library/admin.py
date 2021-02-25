from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'authors', 'price', 'amount')
    list_display = ('title',)
    list_filter = ('price', )
    search_fields = ('title', )
