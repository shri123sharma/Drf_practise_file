# Generated by Django 4.1.3 on 2022-12-14 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_snippet_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
    ]