# Generated by Django 2.2 on 2021-12-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_merge_20211022_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(max_length=15),
        ),
    ]
