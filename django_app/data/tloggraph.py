import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import os
import json
import subprocess

def openfile():
    fileDirectory = os.path.abspath(os.getcwd())
    filename = os.path.join(fileDirectory, '../test_data_w_transactions.json')
    filename2 = os.path.join(fileDirectory, '../dump_state.sh')
    with open(filename) as file:
        data = json.load(file)
    return data

def decisionTrees():
    dataarray = openfile()
    transactionsarray = []
    for array in dataarray:
        if array['fields'] is not None and 'prod_name' in list(array['fields'].keys()):
            print(array['fields'].keys())
            transactionsarray.append(array['fields'])
    producelist = []
    producex = []
    quantityy = []
    for transaction in transactionsarray:
        time = transaction['time'][11:19]
        prodName = transaction['prod_name']
        if prodName not in producelist:
            producelist.append(prodName)
        label = producelist.index(prodName)
        quantity = transaction['quantity']
        hour = time[0:2]
        minute = time[3:5]
        second = time[6:]
        totaltimeinseconds = int(hour) * 3600 + int(minute) * 60 + int(second)
        timeinhours = round(totaltimeinseconds / 3600, 4)
        producex.append([label, timeinhours])
        quantityy.append(quantity)
    regressionmodel = DecisionTreeRegressor(max_depth=3)
    regressionmodel.fit(producex, quantityy)
    numtopredict = 2
    produceitem = producelist[numtopredict]

def pieGraph():
    dataarray = openfile()
    transactionsarray = []
    for array in dataarray:
        if array['fields'] is not None and 'prod_name' in list(array['fields'].keys()):
            transactionsarray.append(array['fields'])
    categorylist = []
    sizes = []
    for transaction in transactionsarray:
        categoryName = transaction['category']
        if 'Misc.' in categoryName or 'None Given' in categoryName:
            categoryName = "Misc."
        if categoryName not in categorylist:
            categorylist.append(categoryName)
        label = categorylist.index(categoryName)
        quantity = 1
        if len(categorylist) != len(sizes):
            sizes.append(quantity)
        else:
            sizes[label] = sizes[label] + quantity
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=categorylist, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title("Quantity of Sales of each item compared to Total Sales")
    plt.savefig('categorypiegraph.png', dpi=500)
    plt.show()
