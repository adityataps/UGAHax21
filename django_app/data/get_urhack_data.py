import tlogapi
import json

all_tlog_summaries = tlogapi.findtlogs()['pageContent']

tlog_ids = {}
for i in range(0,len(all_tlog_summaries)):
    cur_sum = all_tlog_summaries[i]
    tlog_ids[cur_sum['tlogId']] = {
        'dateTime' : cur_sum['endTransactionDateTimeUtc'],
    }

for tlog_id in tlog_ids:
    tlog_data = tlogapi.gettlogbyid(tlog_id)
    tlog = tlog_data['tlog']

    tlog_ids[tlog_id]['site']       = tlog_data['siteInfo']['name']
    tlog_ids[tlog_id]['receiptId']  = tlog['receiptId']
    tlog_ids[tlog_id]['employee']   = tlog['employees'][0]['name']
    tlog_ids[tlog_id]['total_gross'] = tlog['totals']['grossAmount']['amount']
    tlog_ids[tlog_id]['total_grand'] = tlog['totals']['grandAmount']['amount']
    tlog_ids[tlog_id]['order_channel'] = tlog['checkOutType']
    
    tlog_ids[tlog_id]['items'] = []
    item_list = tlog_ids[tlog_id]['items']
    
    for item in tlog['items']:
        #print(item)
        item_dict = {}
        item_dict['id'] = item['id']
        item_dict['prod_id'] = item['productId']
        item_dict['prod_name'] = item['productName']
        item_dict['is_return'] = item['isReturn']
        item_dict['unit_price'] = item['actualUnitPrice']['amount']
        item_dict['quantity'] = item['quantity']['quantity']
        item_dict['unit_of_measure'] = item['quantity']['unitOfMeasurement']
        item_dict['category'] = item['category']['name'] if 'category' in item.keys() else 'None Given'
        item_list.append(item_dict)


    print("Got {} with {} items!".format(tlog_id, len(item_list)))

res_json = json.dumps(tlog_ids)
print(res_json)
