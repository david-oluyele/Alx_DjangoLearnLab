from django.db import models

# Create your models here.
# Author Model: Stores the name of authors.
# Each author can have multiple books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model: Stores book details (title, year) and links to an author.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title