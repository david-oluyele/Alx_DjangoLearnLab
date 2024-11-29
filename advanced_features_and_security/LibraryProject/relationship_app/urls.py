from django.urls import path
from . import views
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'), #Register view
    path('login/', views.login_view, name='login'), #Login view
    path('logout/', views.logout_view, name='logout'), #Logout view

    # Role-based access URLs
    path('admin/', admin_view, name='admin_view'),          # Admin-only view
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian-only view
    path('member/', member_view, name='member_view'),        # Member-only view

    # Other URLs
    path('books/', views.list_books, name='list_books'),           # View for listing all books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Library detail view

    # New URLs for add, edit and delete book
    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # URL for editing a book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # URL for deleting a book
]
