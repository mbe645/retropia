from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'release_year')
    search_fields = ('name', 'platform')
    list_filter = ('platform', 'release_year')
