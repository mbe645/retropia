from django.test import TestCase
from .models import Card

class CardModelTest(TestCase):

    def test_create_pokemon_cards(self):
        Card.objects.create(name="Pikachu", description="Electric-type Pokémon known for agility.", rarity="common")
        Card.objects.create(name="Charizard", description="Fire-type dragon with wings.", rarity="ultra_rare")
        Card.objects.create(name="Mewtwo", description="Legendary psychic Pokémon created in a lab.", rarity="rare")
        self.assertEqual(Card.objects.count(), 3)

    def test_create_yugioh_card(self):
        card = Card.objects.create(name="Dark Magician", description="Yugi’s signature spellcaster.", rarity="rare")
        self.assertEqual(str(card), "Dark Magician (Rare)")

    def test_create_bakugan_card(self):
        card = Card.objects.create(name="Drago", description="Fire element Bakugan.", rarity="rare")
        self.assertTrue("Fire" in card.description)

    def test_rarity_display(self):
        card = Card.objects.create(name="Black Lotus", description="Most valuable MTG card.", rarity="mythic_rare")
        self.assertEqual(str(card), "Black Lotus (Mythic Rare)")
