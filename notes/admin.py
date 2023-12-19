# notes/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Note


class CustomUserAdmin(UserAdmin):
    list_display = ('username',)
    search_fields = ('username',)

    def get_queryset(self, request):
        # Показывать только обычных пользователей, исключая суперпользователей
        return super().get_queryset(request).filter(is_superuser=False)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'user__username')
