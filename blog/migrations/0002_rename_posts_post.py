# Generated by Django 5.0.6 on 2024-06-13 04:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="posts",
            new_name="Post",
        ),
    ]
