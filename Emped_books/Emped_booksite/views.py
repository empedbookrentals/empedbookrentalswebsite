from django.shortcuts import render
from .models import *
from django.http import Http404
from django.http import HttpResponse
# Create your views here.


def main_func(request):
	""" Getting all available books"""

	books = Book.objects.filter(Status__exact='Avl')
	genres = Category.objects.all()
	agerange = Range.objects.all()
	authors = Author.objects.all()
	return render(request, 'Emped_booksite/home.html', {'books': books, 'genres': genres, 'agerange': agerange, 'authors': authors})


def profile_page(request):
	return render(request, 'Emped_booksite/profile.html')


def book_details_view(request, pk):
	try:
		book = Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		raise Http404('Oops Sorry! Book does not exist!!!')
	return render(request, 'Emped_booksite/book_details.html', {'book': book})


def genres_details_view(request, pk):
	try:
		genre = Category.objects.filter(pk=pk)
		try:
			books = Book.objects.filter(Genre=pk)
		except Book.DoesNotExist:
			raise Http404('Oops Sorry! Books does not exist for this Genre!!!')
	except Category.DoesNotExist:
		raise Http404('Oops Sorry! This Genre is temporarily not available!!!')
	return render(request, 'Emped_booksite/genre_details.html', {'books': books, 'genre': genre})


def range_details_view(request, pk):
	try:
		range = Range.objects.filter(pk=pk)
		try:
			books = Book.objects.filter(Genre=pk)
		except Book.DoesNotExist:
			raise Http404('Oops Sorry! Books does not exist for this Range!!!')
	except Range.DoesNotExist:
		raise Http404('Oops Sorry! Book does not exist!!!')
	return render(request, 'Emped_booksite/range_details.html', {'books': books, 'range': range})


def author_details_view(request, pk):
	try:
		authors = Author.objects.filter(pk=pk)
		try:
			books = Book.objects.filter(Genre=pk)
		except Book.DoesNotExist:
			raise Http404('Oops Sorry! Books does not exist for this Range!!!')
	except Author.DoesNotExist:
		raise Http404('Oops Sorry! Book does not exist!!!')
	return render(request, 'Emped_booksite/author_details.html', {'books': books, 'authors': authors})
