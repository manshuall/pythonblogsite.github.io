# Generated by Django 3.2.5 on 2021-08-20 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name': 'Blog'},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 20, 9, 44, 8, 119209)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 8, 20, 4, 14, 8, 119209, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='blogs',
            table='blog_app_blogs',
        ),
    ]
