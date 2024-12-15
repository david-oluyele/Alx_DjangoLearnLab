from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your custom views

urlpatterns = [
    # URL pattern for login
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # URL pattern for logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # URL pattern for user registration
    path('register/', views.register, name='register'),
    
    # URL pattern for user profile
    path('profile/', views.profile, name='profile'),
]
