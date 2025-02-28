import django
import os

# Set up Django environment to use ORM in a standalone script
os.environ['DJANGO_SETTINGS_MODULE'] = 'LibraryProject.settings'
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Test the queries
if __name__ == "__main__":
    # Replace with valid names in your database
    author_name = "Author Name"  # Replace with an actual author's name
    library_name = "Library Name"  # Replace with an actual library name

    print(f"Books by {author_name}:")
    books_by_author = get_books_by_author(author_name)
    if books_by_author:
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print("No books found for the specified author.")

    print(f"\nBooks in {library_name}:")
    books_in_library = get_books_in_library(library_name)
    if books_in_library:
        for book in books_in_library:
            print(f"- {book.title}")
    else:
        print("No books found in the specified library.")

    print(f"\nLibrarian for {library_name}:")
    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"- {librarian.name}")
    else:
        print("No librarian found for the specified library.")

