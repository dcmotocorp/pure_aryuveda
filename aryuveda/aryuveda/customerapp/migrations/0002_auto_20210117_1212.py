# Generated by Django 3.1.5 on 2021-01-17 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cartitem',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
