from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Helper functions to check user role
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin View - Only accessible by users with 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian View - Only accessible by users with 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member View - Only accessible by users with 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')



# Example:
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_list.html', {'books': books})

