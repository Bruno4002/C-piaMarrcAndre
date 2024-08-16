# Generated by Django 5.0.2 on 2024-08-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_livro_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="editora",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
