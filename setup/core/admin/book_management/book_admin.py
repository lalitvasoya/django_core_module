from django.contrib import admin

from core.models.book_management.book_models import Book

@admin.register(Book)
class CustomBookAdmin(admin.ModelAdmin):
    pass
