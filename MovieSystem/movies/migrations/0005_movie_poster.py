# Generated by Django 5.1.3 on 2024-12-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_price_screening_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default=1, upload_to='images/movies_posters/'),
            preserve_default=False,
        ),
    ]
