from django.contrib import admin

from core.models.user_management.user_models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
