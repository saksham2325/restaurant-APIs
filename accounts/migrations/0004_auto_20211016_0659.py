# Generated by Django 2.2 on 2021-10-16 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211015_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updatedat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
