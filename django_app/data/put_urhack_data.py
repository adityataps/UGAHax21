import json
from .models import Transaction, TransactionItem

with open('res.json') as f:
    data = json.load(f)

tlogs = data

for tlid in tlogs.keys():
    tlog = tlogs[tlid]
    
    site = tlog['site']
    receiptId = tlog['receiptId']
    employee = tlog['employee']
    total_gross = tlog['total_gross']
    total_grand = tlog['total_grand']
    order_channel = tlog['order_channel']
    time = tlog['dateTime']

    transaction = Transaction(
                    tid = tlid,
                    site = site,
                    receiptId = receiptId,
                    employee = employee,
                    total_gross = total_gross,
                    total_grand = total_grand,
                    order_channel = order_channel,
                    time = time)

    transaction.save()

    for item in tlog['items']:
        ti_id = item['id']
        prod_id = item['prod_id']
        prod_name = item['prod_name']
        is_return = item['is_return']
        unit_price = item['unit_price']
        unit_of_measure = item['unit_of_measure']
        category = item['category']


        tr_item = TransactionItem(
                    ti_id = ti_id,
                    transaction = transaction,
                    prod_id = prod_id,
                    prod_name = prod_name,
                    is_return = is_return,
                    unit_price = unit_price,
                    unit_of_measure = unit_of_measure,
                    category = category)
        tr_item.save()
    
