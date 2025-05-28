from django.db import models

class Card(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('ultra_rare', 'Ultra Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('mythic_rare', 'Mythic Rare'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rarity = models.CharField(
        max_length=20,
        choices=RARITY_CHOICES,
        default='common'
    )

    def __str__(self):
        return f"{self.name} ({self.get_rarity_display()})"
