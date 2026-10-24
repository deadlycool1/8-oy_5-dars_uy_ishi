from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import DjangoModelPermissions

from .models import Janr, Book, Comment
from .serializers import JanrSerializer, BookSerializer, CommentSerializer
from .permissions import IsCommentOwner


class JanrListCreateView(generics.ListCreateAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer


class JanrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("genre").all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("genre").all()
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related("book", "user").all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        DjangoModelPermissions
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related("book", "user").all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        DjangoModelPermissions,
        IsCommentOwner
    ]
