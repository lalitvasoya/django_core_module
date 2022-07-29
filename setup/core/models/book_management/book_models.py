from django.db import models


class Book(models.Model):
    author_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
