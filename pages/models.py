from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:page-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
