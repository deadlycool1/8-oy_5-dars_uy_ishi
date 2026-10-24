from rest_framework import serializers
from .models import Janr, Book, Comment


class JanrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = "__all__"
        read_only_fields = ["id"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
        read_only_fields = ["id"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "book", "user", "text", "created_at"]
        read_only_fields = ["id", "user", "created_at"]
