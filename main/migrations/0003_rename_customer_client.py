# Generated by Django 4.1.2 on 2022-10-28 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customer_order_delete_cross'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Client',
        ),
    ]
