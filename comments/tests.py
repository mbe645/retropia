from django.test import TestCase
from django.contrib.auth.models import User
from cards.models import Card
from blog.models import BlogPost
from comments.models import Comment
from games.models import Game

class CommentModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a test game (required for Card)
        self.game = Game.objects.create(
            name="Pokémon Red/Blue",
            description="Classic RPG",
            release_year=1996,
            platform="Game Boy"
        )

        # Create a test card
        self.card = Card.objects.create(
            name="Pikachu",
            description="Electric Pokémon",
            rarity="common",
            game=self.game
        )

        # Create a test blog post
        self.blog_post = BlogPost.objects.create(
            title="Top 5 Rare Pokémon Cards",
            content="These are the rarest cards.",
            author=self.user
        )

    def test_comment_on_card(self):
        comment = Comment.objects.create(
            user=self.user,
            content="This card is awesome!",
            card=self.card
        )
        self.assertEqual(comment.card, self.card)
        self.assertEqual(str(comment), f"Comment by {self.user.username} on {self.card}")

    def test_comment_on_blog_post(self):
        comment = Comment.objects.create(
            user=self.user,
            content="Great article!",
            blog_post=self.blog_post
        )
        self.assertEqual(comment.blog_post, self.blog_post)
        self.assertEqual(str(comment), f"Comment by {self.user.username} on {self.blog_post}")
