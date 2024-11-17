from .models import Author, Book, Library

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        # Get the author instance by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author
        books_by_author = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# 2. List all books in a library
def list_books_in_library(library_name):
    try:
        # Get the library instance by name
        library = Library.objects.get(name=library_name)
        
        # Access all books in this library
        books_in_library = library.books.all()
        
        print(f"Books in library '{library_name}':")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        # Get the library instance by name
        library = Library.objects.get(name=library_name)
        
        # Access the librarian assigned to this library
        librarian = library.librarian
        print(f"The librarian for '{library_name}' is: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Library.librarian.RelatedObjectDoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'.")

# Example usage (replace with actual names when testing)
if __name__ == "__main__":
    get_books_by_author("Author Name")
    list_books_in_library("Library Name")
    get_librarian_for_library("Library Name")
