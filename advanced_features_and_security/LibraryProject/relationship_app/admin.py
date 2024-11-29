from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

# Register models for the admin interface
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# Custom admin configuration for the UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display user and role in the list view
    search_fields = ('user__username',)  # Allow searching by username
    list_filter = ('role',)  # Filter by role (Admin, Librarian, Member)

# Register the UserProfile model with the custom UserProfileAdmin class
admin.site.register(UserProfile, UserProfileAdmin)

