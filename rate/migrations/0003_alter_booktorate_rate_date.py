# Generated by Django 4.0.4 on 2022-06-25 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_booktorate_uploading_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktorate',
            name='rate_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
