# Generated by Django 3.1.6 on 2021-02-07 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210206_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='items',
        ),
        migrations.AddField(
            model_name='transactionitem',
            name='transaction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.transaction'),
            preserve_default=False,
        ),
    ]
