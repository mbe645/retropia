# Generated by Django 5.2.1 on 2025-05-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('release_year', models.PositiveIntegerField(blank=True, null=True)),
                ('platform', models.CharField(choices=[('PC', 'PC'), ('Console', 'Console'), ('Arcade', 'Arcade'), ('Mobile', 'Mobile'), ('Other', 'Other')], default='Other', max_length=20)),
            ],
        ),
    ]
