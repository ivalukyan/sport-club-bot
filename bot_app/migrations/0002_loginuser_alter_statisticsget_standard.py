# Generated by Django 5.0.6 on 2024-07-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='')),
                ('password', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='statisticsget',
            name='standard',
            field=models.TextField(default=''),
        ),
    ]
