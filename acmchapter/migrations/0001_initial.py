# Generated by Django 3.1.1 on 2020-12-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Past',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('event', models.CharField(max_length=20)),
                ('attendees', models.IntegerField()),
                ('details', models.TextField(blank=True)),
                ('speaker', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Upcomming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
    ]
