# Generated by Django 4.0.4 on 2022-06-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookToRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('rate_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]