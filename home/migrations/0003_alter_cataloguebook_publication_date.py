# Generated by Django 4.0.4 on 2022-06-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_cataloguebook_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataloguebook',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
