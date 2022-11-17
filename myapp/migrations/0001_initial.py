# Generated by Django 4.1.3 on 2022-11-17 01:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('applicant_id', models.AutoField(default='0', editable=False, primary_key=True, serialize=False)),
                ('applicant_given_name', models.CharField(max_length=30)),
                ('applicant_family_name', models.CharField(max_length=30)),
                ('applicant_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_site', models.CharField(max_length=20)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.applicant')),
            ],
        ),
    ]