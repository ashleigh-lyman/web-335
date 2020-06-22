
#============================================
# Title:  Assignment 9.2 - query through python
# Author: Ashleigh Lyman
# Date:   22 June 2020
# Description: Exercise 9.2 - Python query on mongodb
#===========================================



from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

user={
    "first_name": "Ashleigh",
    "last_name": "Lyman",
    "email": "lyman@email.com",
    "employee_id": "00000001",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "00000001"}))