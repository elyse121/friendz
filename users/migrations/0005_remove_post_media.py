# Generated by Django 5.1.2 on 2025-03-20 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_post_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
    ]
