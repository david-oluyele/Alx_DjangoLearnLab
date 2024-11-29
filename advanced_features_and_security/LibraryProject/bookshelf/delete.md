# delete.md

```python
from bookshelf.models import Book

# Assuming you have already retrieved the book instance
retrieved_book.delete()

# Check if all books are deleted
Book.objects.all()
# Expected output: <QuerySet []>