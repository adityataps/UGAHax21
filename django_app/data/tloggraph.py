import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import os
import json
import numpy as np
import subprocess

def openfile():
    fileDirectory = os.path.abspath(os.getcwd())
    filename = os.path.join(fileDirectory, '../test_data_w_transactions.json')
    with open(filename) as file:
        data = json.load(file)
    return data

def openresfile():
    with open('res.json') as file:
        data = json.load(file)
    return data

def decisionTrees():
    dataarray = openresfile()
    transactionsarray = []
    for arraykey in dataarray.keys():
        array = dataarray[arraykey]
        dateTime = array['dateTime']
        print(dateTime)
        itemlists = array['items']
        if len(itemlists) > 0:
            itemgonethrough = []
            for item in itemlists:
                quantity = 0
                prodName = item['prod_name']
                if item['category'] == "Liquor":
                    if prodName not in itemgonethrough:
                        for item in itemlists:
                            if item['prod_name'] == prodName:
                                quantity = quantity + 1
                        transactionsarray.append([dateTime, prodName, quantity])
                        itemgonethrough.append(prodName)
    producelist = []
    producex = []
    quantityy = []
    for transaction in transactionsarray:
        time = transaction[0][11:19]
        prodName = transaction[1]
        if prodName not in producelist:
            producelist.append(prodName)
        label = producelist.index(prodName)
        quantity = transaction[2]
        hour = time[0:2]
        minute = time[3:5]
        second = time[6:]
        totaltimeinseconds = int(hour) * 3600 + int(minute) * 60 + int(second)
        timeinhours = round(totaltimeinseconds / 3600, 4)
        producex.append(timeinhours)
        quantityy.append(quantity)
    producex = np.array(producex)
    quantityy = np.array(quantityy)
    """
    regressionmodel = DecisionTreeRegressor(max_depth=3)
    regressionmodel.fit(producex.reshape(-1, 1), quantityy.reshape(-1, 1))
    """
    plt.scatter(producex, quantityy)
    plt.title("Average Liquor Items in Each Transaction")
    plt.xlabel("Time From 12am EST")
    plt.ylabel("Quantity")
    plt.show()

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
