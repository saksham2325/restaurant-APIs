# Generated by Django 2.2 on 2021-12-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_merge_20211022_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Rejected'), (1, 'Accepted'), (2, 'Dispatched'), (3, 'Delivered'), (4, 'Cancelled'), (5, 'Placed')], default=5),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='zipcode',
            field=models.CharField(max_length=15),
        ),
    ]