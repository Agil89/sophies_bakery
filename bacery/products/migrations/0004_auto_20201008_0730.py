# Generated by Django 3.1.2 on 2020-10-08 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201007_1547'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutProject',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]