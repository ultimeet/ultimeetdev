# Generated by Django 4.2.2 on 2023-06-24 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='session',
            table='session',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]