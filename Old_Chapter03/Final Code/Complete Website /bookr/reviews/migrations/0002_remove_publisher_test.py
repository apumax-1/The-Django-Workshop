# Generated by Django 3.0a1 on 2019-09-13 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='test',
        ),
    ]