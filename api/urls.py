
from django.urls import path
from .views import (
    JanrListCreateView,
    JanrDetailView,
    BookListCreateView,
    BookDetailView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path("genres/", JanrListCreateView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", JanrDetailView.as_view(), name="genre-detail"),

    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    path("comments/", CommentListCreateView.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
