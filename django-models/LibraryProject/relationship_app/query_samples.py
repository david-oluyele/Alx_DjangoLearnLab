from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"  # replace with the actual author name
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name = "Library Name"  # replace with the actual library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name=library_name)
print(f"Librarian for {library_name}: {librarian_for_library.name}")
