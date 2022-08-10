from django.db import models
from core.models.author_management.author_models import Author


class Book(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
