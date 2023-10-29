# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:13:50 2023

@author: Krishna
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


#Connection request, mongodb+srv://<username>:<password>@<cluster> | Format needs to be URL encoded
uri="mongodb+srv://heraquijiro:44h4X2bycsdPCu7Z@sandbox1.wdeo2cs.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    
    dbInstaSpm = client["InstaSpam"] #Creating DB named InstaSpam
    cltnAccounts = dbInstaSpm["SpamAccounts"] #Creating collection/table called SpamAccounts inside InstaSpam
    
    #Creation start
    '''accountList = [
      { "name": "Amy", "address": "Apple st 652","age":53},
      { "name": "Hannah", "address": "Mountain 21","age":14},
      { "name": "Michael", "address": "Valley 345","age":8},
      { "name": "Sandy", "address": "Ocean blvd 2","age":6},
      { "name": "Betty", "address": "Green Grass 1","age":42},
      { "name": "Richard", "address": "Sky st 331","age":31},
      { "name": "Susan", "address": "One way 98","age":23},
      { "name": "Vicky", "address": "Yellow Garden 2","age":66},
      { "name": "Ben", "address": "Park Lane 38","age":15},
      { "name": "William", "address": "Central st 954","age":3},
      { "name": "Chuck", "address": "Main Road 989","age":62},
      { "name": "Viola", "address": "Sideway 1633","age":40},
      { "name": "Ben", "address": "Park New 38","age":38}
    ]

    pObj = cltnAccounts.insert_many(accountList)'''
    #Creation end
    
    '''for account in cltnAccounts.find({"age":{"$gt":40}},{"name":1}):
        print(account['name'])'''
    
except Exception as e:
    print(e)