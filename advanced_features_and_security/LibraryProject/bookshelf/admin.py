# Register your models here.

# bookshelf/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# Registering the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Specify fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filtering by publication year
    list_filter = ('publication_year',)

    # Enable search by title and author fields
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)