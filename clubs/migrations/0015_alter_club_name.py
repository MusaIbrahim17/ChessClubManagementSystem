# Generated by Django 3.2.5 on 2021-11-24 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0014_alter_membership_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Club name must start with a letter and contain only letters, number, and spaces.', regex='[a-zA-Z][[a-zA-Z0-9 ]+')]),
        ),
    ]
