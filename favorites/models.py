from django.db import models
from django.contrib.auth.models import User
from cards.models import Card
from games.models import Game
from blog.models import BlogPost

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='favorited_by', null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='favorited_by', null=True, blank=True)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='favorited_by', null=True, blank=True)

    class Meta:
        unique_together = (
            ('user', 'card'),
            ('user', 'game'),
            ('user', 'blog'),
        )

    def __str__(self):
        if self.card:
            return f"{self.user.username} favorited card {self.card.name}"
        elif self.game:
            return f"{self.user.username} favorited game {self.game.name}"
        elif self.blog:
            return f"{self.user.username} favorited blog {self.blog.title}"
        return f"{self.user.username} favorited something"
