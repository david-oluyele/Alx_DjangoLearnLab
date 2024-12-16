from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your custom views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    # URL pattern for login
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # URL pattern for logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # URL pattern for user registration
    path('register/', views.register, name='register'),
    
    # URL pattern for user profile
    path('profile/', views.profile, name='profile'),

    path('posts/', PostListView.as_view(), name='post-list'), # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'), # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'), # Edit an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete a post

        # Comment CRUD
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:post_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('post/<int:post_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]