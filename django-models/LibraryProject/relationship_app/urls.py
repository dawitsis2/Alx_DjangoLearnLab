# urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, list_books, add_book, edit_book, delete_book

urlpatterns = [
    # Authentication URLs
    path('register/', register, name='register'),  # User registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User logout

    # Book-related URLs
    path('books/', list_books, name='list_books'),  # List all books
    path('books/add/', add_book, name='add_book'),  # Add a new book
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # Edit an existing book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),  # Delete a book
]
