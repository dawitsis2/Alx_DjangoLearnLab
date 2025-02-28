from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name  # Display author's name in admin and queries


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Book linked to an Author
    publication_date = models.DateField()  # Optional: Add publication date
    isbn = models.CharField(max_length=13, unique=True)  # Optional: Unique ISBN
    summary = models.TextField(blank=True)  # Optional: Summary of the book

    def __str__(self):
        return self.title  # Display book title in admin and queries


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=200)  # Name of the library
    books = models.ManyToManyField(Book)  # Library has many books

    def __str__(self):
        return self.name  # Display library name in admin and queries


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Name of the librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # Each library has one librarian

    def __str__(self):
        return self.name  # Display librarian's name in admin and queries

