from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(ListAPIView):
    """API view to retrieve a list of books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer