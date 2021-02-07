from rest_framework import serializers

from .models import Transaction, TransactionItem

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('tid', 'site', 'tnum', 'receiptId', 'employee', 'total_gross', 'total_grand', 'order_channel', 'time')

class TransactionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionItem
        fields = ('ti_id', 'transaction', 'prod_id', 'prod_name', 'is_return', 'unit_price', 'quantity', 'unit_of_measure', 'category')
