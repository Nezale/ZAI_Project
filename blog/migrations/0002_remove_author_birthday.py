# Generated by Django 3.2.3 on 2021-05-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birthday',
        ),
    ]
