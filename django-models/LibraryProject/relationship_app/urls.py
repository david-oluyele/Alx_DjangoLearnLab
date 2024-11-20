from django.urls import path
from . import views
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-based access URLs
    path('admin/', admin_view, name='admin_view'),          # Admin-only view
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian-only view
    path('member/', member_view, name='member_view'),        # Member-only view

    # Other URLs
    path('books/', views.list_books, name='list_books'),           # View for listing all books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Library detail view
]
