from django.db import models
from django.contrib.auth.models import User
from cards.models import Card

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'card')  # To same user can only favorite the same card once

    def __str__(self):
        return f"{self.user.username} favorited {self.card.name}"
