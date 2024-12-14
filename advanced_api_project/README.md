# Documentaion for advanced_api_project

# Models Documentation
Author model represents authors with a one-to-many relationship to the Book model.
Book model includes a title, a publication year, and a foreign key to an author.

# Serializers Documentation
BookSerializer handles serialization for the Book model, including validation for publication_year.
AuthorSerializer serializes the Author model, including a nested BookSerializer for related books.