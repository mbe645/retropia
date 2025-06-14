# Generated by Django 5.2 on 2025-06-01 07:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogcomment_blog'),
        ('cards', '0003_remove_card_game'),
        ('favorites', '0001_initial'),
        ('games', '0003_gamecomment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'card')},
        ),
        migrations.AddField(
            model_name='favorite',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='blog.blogpost'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='games.game'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='cards.card'),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'blog'), ('user', 'card'), ('user', 'game')},
        ),
    ]
