import requests
from datetime import datetime
import hashlib
import pythonHmacSnippet
import json
from datetime import timezone


def createorder():
    bsporgkey = 'f62afa5aab2d4a249cd88c6e0eb1a733'
    bspsecretkey = 'aab8e7d75ce74748ae07f39bf990aa8a'
    bspsharedkey = 'fa24bf888a8647bbb5bfd4d35cd73fd1'
    bspsiteid = '9122a304a3444db984ea21beaf315c1d'
    date = datetime.now(tz=timezone.utc)
    date = datetime(date.year, date.month, date.day, hour=date.hour,
               minute=date.minute, second=date.second)
    isoDate = date.isoformat(timespec='milliseconds') + 'Z'
    utcDate = date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    requesturl = 'https://gateway-staging.ncrcloud.com/order/3/orders/1'
    accesskey = pythonHmacSnippet.createHMAC(sharedKey=bspsharedkey,
                                             secretKey=bspsecretkey,
                                             dateHeader=isoDate,
                                             httpMethod="POST",
                                             requestURL=requesturl,
                                             contentType='application/json',
                                             contentMD5=None,
                                             nepOrganization=bsporgkey,
                                             nepApplicationKey=None,
                                             nepCorrelationID=None,
                                             nepServiceVersion=None)
    data = {
        "expireAt": "2020-05-08T14:26:48Z",
        "comments": "Good-Morning"
    }

    payload = json.dumps(data)

    headers = {'Content-type': 'application/json', 'Authorization': accesskey,
               'nep-organization': bsporgkey, 'nep-enterprise-unit': bspsiteid,
               'Date': utcDate}
    response = requests.post(requesturl, payload, headers=headers)
    return response.json()

def getorderbyid(orderid):
    bsporgkey = 'f62afa5aab2d4a249cd88c6e0eb1a733'
    bspsecretkey = 'aab8e7d75ce74748ae07f39bf990aa8a'
    bspsharedkey = 'fa24bf888a8647bbb5bfd4d35cd73fd1'
    bspsiteid = '9122a304a3444db984ea21beaf315c1d'
    date = datetime.now(tz=timezone.utc)
    date = datetime(date.year, date.month, date.day, hour=date.hour,
               minute=date.minute, second=date.second)
    isoDate = date.isoformat(timespec='milliseconds') + 'Z'
    utcDate = date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    requesturl = 'https://gateway-staging.ncrcloud.com/order/3/orders/1/{0}'.format(orderid)
    accesskey = pythonHmacSnippet.createHMAC(sharedKey=bspsharedkey,
                                             secretKey=bspsecretkey,
                                             dateHeader=isoDate,
                                             httpMethod="GET",
                                             requestURL=requesturl,
                                             contentType='application/json',
                                             contentMD5=None,
                                             nepOrganization=bsporgkey,
                                             nepApplicationKey=None,
                                             nepCorrelationID=None,
                                             nepServiceVersion=None)
    headers = {'Content-type': 'application/json', 'Authorization': accesskey,
               'nep-organization': bsporgkey, 'nep-enterprise-unit': bspsiteid,
               'Date': utcDate}
    response = requests.get(requesturl, headers=headers)
    return response.json()

def findorders():
    bsporgkey = 'f62afa5aab2d4a249cd88c6e0eb1a733'
    bspsecretkey = 'aab8e7d75ce74748ae07f39bf990aa8a'
    bspsharedkey = 'fa24bf888a8647bbb5bfd4d35cd73fd1'
    bspsiteid = '9122a304a3444db984ea21beaf315c1d'
    date = datetime.now(tz=timezone.utc)
    date = datetime(date.year, date.month, date.day, hour=date.hour,
               minute=date.minute, second=date.second)
    isoDate = date.isoformat(timespec='milliseconds') + 'Z'
    utcDate = date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    requesturl = 'https://gateway-staging.ncrcloud.com/order/3/orders/1/find'
    accesskey = pythonHmacSnippet.createHMAC(sharedKey=bspsharedkey,
                                             secretKey=bspsecretkey,
                                             dateHeader=isoDate,
                                             httpMethod="POST",
                                             requestURL=requesturl,
                                             contentType='application/json',
                                             contentMD5=None,
                                             nepOrganization=bsporgkey,
                                             nepApplicationKey=None,
                                             nepCorrelationID=None,
                                             nepServiceVersion=None)

    data = { }
    payload = json.dumps(data)
    headers = {'Content-type': 'application/json', 'Authorization': accesskey,
               'nep-organization': bsporgkey, 'nep-enterprise-unit': bspsiteid,
               'Date': utcDate}
    response = requests.post(requesturl, payload, headers=headers)
    return response.json()