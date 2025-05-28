from django.test import TestCase
from .models import Game

class GameModelTest(TestCase):

    def test_create_super_mario(self):
        game = Game.objects.create(
            name="Super Mario Bros",
            description="Classic platformer game",
            release_year=1985,
            platform="NES"
        )
        self.assertEqual(game.name, "Super Mario Bros")
        self.assertEqual(game.release_year, 1985)
        self.assertEqual(game.platform, "NES")

    def test_create_sonic(self):
        game = Game.objects.create(
            name="Sonic the Hedgehog",
            description="Fast-paced side-scroller",
            release_year=1991,
            platform="Sega Genesis"
        )
        self.assertEqual(game.platform, "Sega Genesis")

    def test_create_pacman(self):
        game = Game.objects.create(
            name="Pac-Man",
            description="Maze-based arcade game",
            release_year=1980,
            platform="Arcade"
        )
        self.assertTrue("Pac" in game.name)

    def test_create_gta_vice_city(self):
        game = Game.objects.create(
            name="GTA: Vice City",
            description="Open-world action-adventure",
            release_year=2002,
            platform="PlayStation 2"
        )
        self.assertEqual(game.release_year, 2002)
        self.assertEqual(game.platform, "PlayStation 2")
