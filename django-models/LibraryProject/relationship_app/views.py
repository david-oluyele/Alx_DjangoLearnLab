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

# Helper function to check if a user is an Admin
def is_admin(user):
    """Checks if the user has an 'Admin' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin view - only accessible by users with 'Admin' role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Helper function to check if a user is a Librarian
def is_librarian(user):
    """Checks if the user has a 'Librarian' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian view - only accessible by users with 'Librarian' role
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Helper function to check if a user is a Member
def is_member(user):
    """Checks if the user has a 'Member' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Member view - only accessible by users with 'Member' role
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
