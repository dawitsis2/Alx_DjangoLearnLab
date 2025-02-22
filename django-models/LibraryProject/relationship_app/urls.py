# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books, LibraryDetailView, register, login_view, logout_view,
    admin_view, librarian_view, member_view, edit_profile,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # Book-related URLs
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),

    # Library-related URLs
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # User authentication URLs
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # Use custom login view
    path('logout/', logout_view, name='logout'),  # Use custom logout view

    # Role-based URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    # Profile-related URLs
    path('edit_profile/', edit_profile, name='edit_profile'),
]
