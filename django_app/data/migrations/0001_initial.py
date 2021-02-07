# Generated by Django 3.1.6 on 2021-02-06 23:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionItem',
            fields=[
                ('ti_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('prod_id', models.IntegerField()),
                ('prod_name', models.CharField(max_length=120)),
                ('is_return', models.BooleanField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('site', models.CharField(max_length=100)),
                ('tnum', models.IntegerField()),
                ('receiptId', models.IntegerField()),
                ('employee', models.CharField(max_length=120)),
                ('total_gross', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_grand', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_channel', models.CharField(max_length=50)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.transactionitem')),
            ],
        ),
    ]
