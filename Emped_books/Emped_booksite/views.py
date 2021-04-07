from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def main_func(request):
	""" Getting all available books"""
	books = Book.objects.filter(Status__exact='Avl')
	genres = Category.objects.all()
	return render(request, 'Emped_booksite/home.html', {'books': books, 'genres': genres})


def profile_page(request):
	return render(request, 'Emped_booksite/profile.html')
