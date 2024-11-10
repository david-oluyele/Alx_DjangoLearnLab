# CRUD Operations on Book Model

# Create Command 

Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected output: <Book: 1984 by George Orwell (1949)>

# Retrieve Operation
Command:
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
# Expected output: <Book: 1984 by George Orwell (1949)>

# Update Operation
Command:
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete Operation
Command:
```python
retrieved_book.delete()
Book.objects.all()
# Expected output: <QuerySet []>
