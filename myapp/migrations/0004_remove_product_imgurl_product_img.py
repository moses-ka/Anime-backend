# Generated by Django 4.2.7 on 2023-11-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_imgurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imgUrl',
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
