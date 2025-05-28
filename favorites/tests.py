from django.test import TestCase
from django.contrib.auth.models import User
from cards.models import Card
from games.models import Game
from favorites.models import Favorite
from django.db.utils import IntegrityError

class FavoriteModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.game = Game.objects.create(
            name="Yu-Gi-Oh!",
            description="Card battle game",
            release_year=2004,
            platform="PC"
        )

        self.card = Card.objects.create(
            name="Dark Magician",
            description="Iconic spellcaster",
            rarity="rare",
            game=self.game
        )

    def test_add_favorite(self):
        favorite = Favorite.objects.create(user=self.user, card=self.card)
        self.assertEqual(favorite.user, self.user)
        self.assertEqual(favorite.card, self.card)
        self.assertEqual(str(favorite), f"{self.user.username} favorited {self.card.name}")

    def test_duplicate_favorite_not_allowed(self):
        Favorite.objects.create(user=self.user, card=self.card)
        with self.assertRaises(IntegrityError):
            Favorite.objects.create(user=self.user, card=self.card)
