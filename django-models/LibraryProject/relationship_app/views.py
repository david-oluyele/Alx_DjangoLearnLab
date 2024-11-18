# Import necessary modules 
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Book, Library, UserProfile

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs['pk'])

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created successfully.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Custom decorators for role-based access
def admin_required(view_func):
    return login_required(user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'))(view_func)

def librarian_required(view_func):
    return login_required(user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'))(view_func)

def member_required(view_func):
    return login_required(user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Member'))(view_func)

# Admin view - only accessible by users with 'Admin' role
@admin_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - only accessible by users with 'Librarian' role
@librarian_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - only accessible by users with 'Member' role
@member_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
