from django.contrib import admin

from core.models.author_management.author_models import Author

@admin.register(Author)
class CustomAuthorAdmin(admin.ModelAdmin):
    pass
