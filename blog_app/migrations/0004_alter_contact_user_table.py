# Generated by Django 3.2.5 on 2021-08-19 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20210819_2112'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contact_user',
            table='blog_app_contact_user',
        ),
    ]