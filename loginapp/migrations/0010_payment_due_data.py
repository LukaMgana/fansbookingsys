# Generated by Django 3.2.3 on 2021-07-08 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_alter_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='due_data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
