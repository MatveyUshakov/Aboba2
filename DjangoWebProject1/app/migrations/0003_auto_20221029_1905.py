# Generated by Django 2.2.28 on 2022-10-29 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221029_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 10, 29, 19, 5, 48, 273971), verbose_name='Опубликована'),
        ),
    ]
