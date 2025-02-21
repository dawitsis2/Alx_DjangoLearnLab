from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.models import User

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can assign a default role to the user, e.g., "Member"
            UserProfile.objects.create(user=user, role='Member')
            login(request, user)  # Automatically log in the user after registration
            return redirect('member_view')  # Redirect based on the role or a specific page
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# Admin view - accessible only by admin users
@login_required
def admin_view(request):
    if request.user.userprofile.role != 'Admin':
        return redirect('member_view')  # Redirect if the user is not an admin
    return render(request, 'admin_view.html')

# Librarian view - accessible only by librarian users
@login_required
def librarian_view(request):
    if request.user.userprofile.role != 'Librarian':
        return redirect('member_view')  # Redirect if the user is not a librarian
    return render(request, 'librarian_view.html')

# Member view - accessible by all authenticated users
@login_required
def member_view(request):
    return render(request, 'member_view.html')

# Edit Profile view - accessible by all users for editing their profile
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
    return render(request, 'edit_profile.html')

# Manage Roles view - accessible by admin users for assigning roles
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

    return render(request, 'manage_roles.html', {'users': users})


