from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity_stars')
    search_fields = ('name', 'description')
    list_filter = ('rarity',)

    def rarity_stars(self, obj):
        star_map = {
            'common': 1,
            'rare': 2,
            'ultra_rare': 3,
            'epic': 4,
            'legendary': 5,
            'mythic_rare': 5,
        }
        count = star_map.get(obj.rarity, 0)
        return '★' * count + '☆' * (5 - count)

    rarity_stars.short_description = 'Rarity'
