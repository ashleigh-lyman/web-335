#============================================
# Title:  Assignment 9.3 - Python update
# Author: Ashleigh Lyman
# Date:   22 June 2020
# Description: Exercise 9.3 Python update on mongo database
#===========================================


from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    {"employee_id":"0000001"},
    {
        "$set":{
            "email":"lyman@email.com"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id":"0000001"}))