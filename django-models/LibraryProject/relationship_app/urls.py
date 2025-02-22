# relationship_app/urls.py

from django.urls import path
from .views import list_books, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]

