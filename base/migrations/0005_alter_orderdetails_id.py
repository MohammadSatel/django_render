# Generated by Django 4.2.6 on 2023-11-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_orderdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
