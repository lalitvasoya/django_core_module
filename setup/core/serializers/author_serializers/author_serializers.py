from datetime import datetime
from rest_framework import serializers
from core.models.author_management.author_models import Author


class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email')
