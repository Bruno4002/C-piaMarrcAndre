# Generated by Django 5.0.2 on 2024-03-12 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_site_editora_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="editora",
            old_name="url",
            new_name="site",
        ),
    ]