from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from . import views
from .views import list_books 

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-based access URLs
    path('admin/', views.admin_view, name='admin_view'),          # Admin-only view
    path('librarian/', views.librarian_view, name='librarian_view'),  # Librarian-only view
    path('member/', views.member_view, name='member_view'),        # Member-only view

    # Other URLs
    path('books/', views.list_books, name='list_books'),           # View for listing all books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Library detail view
]