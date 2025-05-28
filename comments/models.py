from django.db import models
from django.contrib.auth.models import User
from blog.models import BlogPost
from cards.models import Card

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Related content (optional)
    blog_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='comments'
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='comments'
    )

    def __str__(self):
        target = self.blog_post or self.card
        return f"Comment by {self.user.username} on {target}"
