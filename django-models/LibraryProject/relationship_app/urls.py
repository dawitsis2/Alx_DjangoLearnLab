from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import include

urlpatterns = [
    # Login and Logout views
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # Registration view (if you have a registration view for new users)
    path('register/', views.register, name='register'),

    # Role-based access control views
    path('admin/', views.admin_view, name='admin_view'),  # Accessible by Admins only
    path('librarian/', views.librarian_view, name='librarian_view'),  # Accessible by Librarians only
    path('member/', views.member_view, name='member_view'),  # Accessible by Members only

    # Django Admin panel (do not remove this line)
    path('admin/', admin.site.urls),

    # Include other URL patterns (this assumes your app's URLs are located in 'relationship_app.urls')
    path('relationship/', include('relationship_app.urls')),
]

