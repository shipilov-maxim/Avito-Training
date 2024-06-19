from django.contrib import admin

from app.models import Secret


@admin.register(Secret)
class PostAdmin(admin.ModelAdmin):
    list_display = ('_id',)
