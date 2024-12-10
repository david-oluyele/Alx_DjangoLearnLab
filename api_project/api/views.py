from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data

class BookViewSet(ModelViewSet):  # Handles all CRUD operations
    queryset = Book.objects.all()
    serializer_class = BookSerializer
