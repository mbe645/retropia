from django.db import models

class Game(models.Model):
    PLATFORM_CHOICES = [
        ('NES', 'NES'),
        ('Sega Genesis', 'Sega Genesis'),
        ('Arcade', 'Arcade'),
        ('PlayStation 2', 'PlayStation 2'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        default='NES'
    )

    def __str__(self):
        return self.name
