# Generated by Django 4.2.7 on 2024-08-25 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_order_orders_delete_orderedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
