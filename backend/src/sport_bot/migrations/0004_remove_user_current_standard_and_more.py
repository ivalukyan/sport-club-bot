# Generated by Django 5.0.6 on 2024-06-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_bot', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='current_standard',
        ),
        migrations.AddField(
            model_name='profile',
            name='current_standard',
            field=models.TextField(default='No standard'),
        ),
    ]