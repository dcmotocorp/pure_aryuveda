# Generated by Django 3.1.5 on 2021-01-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0006_auto_20210117_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='itemimage',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]