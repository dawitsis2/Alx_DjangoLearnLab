# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Book
from .forms import BookForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect("list_books")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Login successful.")
            return redirect("list_books")
        else:
            messages.error(request, "Unsuccessful login. Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User logout view
def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Add a new book (requires 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully.")
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit an existing book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# Delete a book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
