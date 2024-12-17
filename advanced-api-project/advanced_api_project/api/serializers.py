from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer: Serializes Book model fields and validates the publication_year field.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer with nested BookSerializer
# AuthorSerializer: Serializes Author model fields and nests related books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
