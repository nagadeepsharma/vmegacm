# Generated by Django 3.1.1 on 2020-12-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmchapter', '0003_auto_20201227_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomming',
            name='img',
            field=models.ImageField(blank=True, upload_to='acmchapter/'),
        ),
    ]
