import uuid
from django.db import models

# Create your models here.
class Transaction(models.Model):
    tid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    site = models.CharField(max_length=100)
    tnum = models.IntegerField()
    receiptId = models.IntegerField()
    employee = models.CharField(max_length=120)
    total_gross = models.DecimalField(max_digits=6, decimal_places=2)
    total_grand = models.DecimalField(max_digits=6, decimal_places=2)
    order_channel = models.CharField(max_length=50)
    time = models.DateTimeField()
    
    def __str__(self):
        return "{} - {} @ {}".format(self.tid, self.site, self.time)

class TransactionItem(models.Model):
    ti_id = models.IntegerField(primary_key=True)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=120)
    is_return = models.BooleanField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    unit_of_measure = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} x{} @ {} ea.".format(self.ti_id, self.prod_name, self.quantity, self.unit_price)
    
