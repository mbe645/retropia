from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title
