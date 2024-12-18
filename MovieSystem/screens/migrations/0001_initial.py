# Generated by Django 5.1.3 on 2024-12-02 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater', models.CharField(max_length=200)),
                ('showtime', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seats', models.TextField(default='{"A1": true, "A2": true, "A3": true, "A4": true, "A5": true, "A6": true, "B1": true, "B2": true, "B3": true, "B4": true, "B5": true, "B6": true, "C1": true, "C2": true, "C3": true, "C4": true, "C5": true, "C6": true, "D1": true, "D2": true, "D3": true, "D4": true, "D5": true, "D6": true}')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_numbers', models.JSONField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screens.screening')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
