from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
