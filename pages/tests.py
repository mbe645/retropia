from django.test import TestCase
from pages.models import Page

class PageModelTest(TestCase):

    def setUp(self):
        self.page = Page.objects.create(
            title="About Us",
            content="This is a static page about the Retropia platform."
        )

    def test_page_fields(self):
        self.assertEqual(self.page.title, "About Us")
        self.assertEqual(self.page.content, "This is a static page about the Retropia platform.")

    def test_page_str(self):
        self.assertEqual(str(self.page), "About Us")
