# Generated by Django 5.0.6 on 2024-08-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='book',
            new_name='book_name',
        ),
    ]
