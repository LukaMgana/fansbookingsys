# Generated by Django 3.2.3 on 2021-07-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_auto_20210708_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
