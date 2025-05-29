from django.db import models
from django.contrib.auth.models import User

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

class GameComment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
