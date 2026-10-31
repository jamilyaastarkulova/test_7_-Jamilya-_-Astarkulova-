from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import BookForm
from  webapp.models import Book
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

def index_view(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def book_view(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     # return HttpResponseNotFound('Book not found')
    #     raise Http404('Book not found')
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_view.html', {'book': book})



def book_create_view(request):

    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm(data= request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = form.cleaned_data.get('author')
            book = Article.objects.create(title=title, content=content, author=author)
            return redirect('book_view', pk=book.id)
        else:
            return render(request, 'create_book.html', {'form': form})


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={'title': book.title, 'content': book.content, 'author': book.author})
        return render(request, 'update_book.html', {'book': book, 'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.title = form.cleaned_data.get('title')
            book.content = form.cleaned_data.get('content')
            book.author = form.cleaned_data.get('author')
            book.save()
            return redirect('book_view', pk=book.id)
        else:
            return render(request, 'update_book.html', {'book': book, 'form': form})



def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_book.html', {'book': book})
    elif request.method == "POST":
        book.delete()
        return redirect('book_list')