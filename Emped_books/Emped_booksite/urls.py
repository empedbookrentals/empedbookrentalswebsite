from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.main_func, name='index-page'),
    path(r'profile/', views.profile_page, name='profile-page'),
    path(r'book-details/<int:pk>/', views.book_details_view, name='book-detail'),
    path(r'Genres-details/<int:pk>/', views.genres_details_view, name='Genres-detail'),
    path(r'Range-details/<int:pk>/', views.range_details_view, name='Range-detail'),
    path(r'Author-details/<int:pk>/', views.author_details_view, name='Author-detail'),
    path(r'authenticate/', views.customer_authenticate, name='login'),
]
