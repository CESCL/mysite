# Generated by Django 4.1.3 on 2022-11-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_booking_id_booking_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
