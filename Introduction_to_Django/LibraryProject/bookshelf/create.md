# Create a Book Instance

## Command to Create a Book

To create a book in the Django shell, follow the steps below:

1. Open the Django shell:
   ```bash
   python manage.py shell
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book = Book.objects.get(title="1984")
book.delete()

