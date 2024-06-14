# Generated by Django 5.0.6 on 2024-06-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standards',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('thunder', models.CharField(max_length=50)),
                ('turkish_ascent_axel', models.CharField(max_length=50)),
                ('turkish_ascent_kettlebell', models.CharField(max_length=50)),
                ('bench_press', models.CharField(max_length=50)),
                ('axel_jerk', models.CharField(max_length=50)),
                ('taking_on_axel_chest', models.CharField(max_length=50)),
                ('gluteal_bridge', models.CharField(max_length=50)),
                ('deadlift', models.CharField(max_length=50)),
                ('jerk', models.CharField(max_length=50)),
                ('taking_on_the_chest', models.CharField(max_length=50)),
                ('axel_deadlift', models.CharField(max_length=50)),
                ('classic_squat', models.CharField(max_length=50)),
                ('front_squat', models.CharField(max_length=50)),
                ('squat_over_the_head', models.CharField(max_length=50)),
                ('back_squat', models.CharField(max_length=50)),
                ('skipping_rope', models.CharField(max_length=50)),
                ('push_ups', models.CharField(max_length=50)),
                ('shuttle_running', models.CharField(max_length=50)),
                ('farmer_walk', models.CharField(max_length=50)),
                ('pull_ups', models.CharField(max_length=50)),
                ('high_jump', models.CharField(max_length=50)),
                ('long_jump', models.CharField(max_length=50)),
                ('holding_the_axel', models.CharField(max_length=50)),
                ('handstand', models.CharField(max_length=50)),
            ],
        ),
    ]
