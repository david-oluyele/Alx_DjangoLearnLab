# retrieve.md
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
# Expected output: <Book: 1984 by George Orwell (1949)>
