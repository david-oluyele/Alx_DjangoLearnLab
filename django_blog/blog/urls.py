from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your custom views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # URL pattern for login
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # URL pattern for logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # URL pattern for user registration
    path('register/', views.register, name='register'),
    
    # URL pattern for user profile
    path('profile/', views.profile, name='profile'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]