from django.urls import path
from . import views  # Correct import

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Corrected
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Corrected
]

