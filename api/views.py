from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Janr, Book, Comment
from .serializers import JanrSerializer, BookSerializer, CommentSerializer
from .permissions import IsCommentOwner


class JanrViewSet(viewsets.ModelViewSet):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("genre").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
