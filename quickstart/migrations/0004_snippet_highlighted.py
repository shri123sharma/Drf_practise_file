# Generated by Django 4.1.3 on 2022-12-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_author_blog_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]