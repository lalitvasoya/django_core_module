from datetime import date
from rest_framework import serializers
from core.models.book_management.book_models import Book


class BookModelSerializer(serializers.ModelSerializer):
    publication_date = serializers.DateField(default=date.today)

    class Meta:
        model = Book
        fields = ('id', 'author_id', 'title', 'publication_date')
