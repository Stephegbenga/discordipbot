from pymongo import MongoClient
from decouple import config
from pprint import pprint
dburl = config('db_url')
conn = MongoClient(dburl)

db = conn['supernova-node']

collection = db['discord_users']


def add(data):
    try:
        dataa = collection.insert_one(data)
        pprint(dataa)
        return dataa
    except Exception as e:
        print("An error Occurred")
        pprint(e)


def find(data):
    my_list = []
    for x in collection.find(data):
        my_list.append(x)
    if my_list:
        data = my_list[-1]
        return data


def update(myquery, newvalues):
    dataa = collection.update_one(myquery, {"$set":newvalues})
    return(dataa)


def delete(query):
    dataa = collection.delete_one(query)
    return (dataa)


