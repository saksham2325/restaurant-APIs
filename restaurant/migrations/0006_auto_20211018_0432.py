# Generated by Django 2.2 on 2021-10-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20211016_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Rejected'), (1, 'accepted'), (2, 'dispatched'), (3, 'delivered'), (4, 'cancelled'), (5, 'placed')], default=5),
        ),
    ]