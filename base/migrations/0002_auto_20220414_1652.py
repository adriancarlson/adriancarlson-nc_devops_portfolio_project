# Generated by Django 3.2.2 on 2022-04-14 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='create',
        ),
        migrations.RemoveField(
            model_name='meetings',
            name='updated',
        ),
    ]
