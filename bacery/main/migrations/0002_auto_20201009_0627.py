# Generated by Django 3.1.2 on 2020-10-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.SmallIntegerField(verbose_name='Phone Number'),
        ),
    ]
