# Generated by Django 5.1 on 2024-11-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstblog', '0013_remove_profile_facebook_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
