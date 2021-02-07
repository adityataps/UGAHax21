from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TransactionSerializer, TransactionItemSerializer
from .models import Transaction, TransactionItem

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('tid')
    serializer_class = TransactionSerializer

class TransactionItemViewSet(viewsets.ModelViewSet):
    queryset = TransactionItem.objects.all().order_by('ti_id')
    serializer_class = TransactionItemSerializer
