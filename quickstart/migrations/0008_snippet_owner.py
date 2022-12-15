# Generated by Django 4.1.3 on 2022-12-14 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_user_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_owner', to='quickstart.user_1'),
            preserve_default=False,
        ),
    ]
