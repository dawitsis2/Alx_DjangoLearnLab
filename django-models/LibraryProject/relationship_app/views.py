from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    if request.user.userprofile.role != 'Librarian':
        return redirect('member_view')  # Redirect if the user is not a librarian
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        # Optionally, update the UserProfile as well if needed
        user.userprofile.save()
        return redirect('member_view')  # Redirect after saving profile changes
    return render(request, 'relationship_app/edit_profile.html')

@user_passes_test(is_admin)
@login_required
def manage_roles(request):
    if request.user.userprofile.role != 'Admin':
        return redirect('member_view')  # Redirect if the user is not an admin

    # Get all users and their roles
    users = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role = request.POST.get('role')
        user = User.objects.get(id=user_id)
        user.userprofile.role = role
        user.userprofile.save()
        return redirect('manage_roles')  # Refresh the page after role assignment

    return render(request, 'relationship_app/manage_roles.html', {'users': users})

