# Generated by Django 5.2 on 2025-05-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
