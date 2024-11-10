# Register your models here.

# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Registering the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Specify fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filtering by publication year
    list_filter = ('publication_year',)

    # Enable search by title and author fields
    search_fields = ('title', 'author')

