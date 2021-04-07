from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_func, name='index-page'),
    path('profile/', views.profile_page, name='profile-page'),
]
