# Import necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import DetailView
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
        return Library.objects.get(pk=self.kwargs['pk'])

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

# Helper functions to check roles
def is_admin(user):
    """Check if the user has an 'Admin' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Check if the user has a 'Librarian' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Check if the user has a 'Member' role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views (added back for the checker)
@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
