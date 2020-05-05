from .views import (BookListView, BookDetailView)
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('<int:id>/', BookDetailView.as_view(), name='book-detail'),
]
