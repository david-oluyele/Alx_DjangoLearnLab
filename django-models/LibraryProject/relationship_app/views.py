from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
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

# Role-based views (removed for brevity)

# View to add a new book - only users with 'can_add_book' permission
@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    # Logic for adding a new book
    return render(request, 'relationship_app/add_book.html')

# View to edit a book - only users with 'can_change_book' permission
@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # Logic for editing the book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to delete a book - only users with 'can_delete_book' permission
@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # Logic for deleting the book
    return render(request, 'relationship_app/delete_book.html', {'book': book})
