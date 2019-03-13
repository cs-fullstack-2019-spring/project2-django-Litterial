# Generated by Django 2.0.6 on 2019-03-13 14:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikipediaApp', '0006_auto_20190313_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 3, 13, 14, 37, 41, 799569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 3, 13, 14, 37, 41, 799597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='related',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 13, 14, 37, 41, 800315, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='related',
            name='last_update',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 13, 14, 37, 41, 800337, tzinfo=utc)),
        ),
    ]
