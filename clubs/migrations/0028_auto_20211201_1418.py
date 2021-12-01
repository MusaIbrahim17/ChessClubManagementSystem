# Generated by Django 3.2.5 on 2021-12-01 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0027_auto_20211127_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='mission_statement',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='chess_experience',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('M', 'Master'), ('G', 'Grandmaster')], default='B', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='public_bio',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]