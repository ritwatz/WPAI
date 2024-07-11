from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def insert_book(request):
    return render(request, 'insert.html')


def book_input(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('pub_date')
        book = Book(title=title, author=author, published_date=published_date)
        book.save()
        return HttpResponse('received')
    else:
        return HttpResponse('invalid method')