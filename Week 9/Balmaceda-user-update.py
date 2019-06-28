#============================================
# Title:  calculator
# Author: Griselda Balmaceda 
# Date:   27 June 2019
# Description: Updating user 
#===========================================
#importing necessary modules 
from pymongo import MongoClient
import pprint
import datetime
#connececting to our mongoDB instance
client = MongoClient('localhost',27017)
#selecting our database
db=client.web335

#updating one of the users email to my school email.
db.users.update_one(
    {"employee_id":"7683994"},
    {"$set":{
        "email":"gzbalmaceda@my365.bellevue.edu"
    }
    }
)
#quering the updated user
pprint.pprint(db.users.find_one({"employee_id":"7683994"}))