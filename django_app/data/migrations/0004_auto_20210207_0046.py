# Generated by Django 3.1.6 on 2021-02-07 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210207_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionitem',
            name='time',
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 0, 46, 20, 11327)),
            preserve_default=False,
        ),
    ]