from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import BlogPost
from django.urls import reverse

class BlogPostModelTest(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create test blog post
        self.blog_post = BlogPost.objects.create(
            title="My First Retro Game Blog",
            content="This is a blog post about retro games.",
            author=self.user
        )

    def test_blog_post_content(self):
        self.assertEqual(self.blog_post.title, "My First Retro Game Blog")
        self.assertEqual(self.blog_post.content, "This is a blog post about retro games.")
        self.assertEqual(self.blog_post.author.username, "testuser")

    def test_blog_post_str(self):
        self.assertEqual(str(self.blog_post), "My First Retro Game Blog")

    def test_get_absolute_url(self):
        url = self.blog_post.get_absolute_url()
        self.assertEqual(url, reverse('blogpost-detail', args=[str(self.blog_post.id)]))
