# Generated by Django 3.1.1 on 2020-12-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmchapter', '0002_auto_20201227_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='upcomming',
            name='link',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
