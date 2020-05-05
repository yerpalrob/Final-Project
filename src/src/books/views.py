from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import (
    ListView,
    DetailView
)

# Create your views here.


class BookListView(ListView):
    template_name = 'books/index.html'
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    queryset = Book.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)
