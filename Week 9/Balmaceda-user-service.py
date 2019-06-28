#============================================
# Title:  calculator
# Author: Griselda Balmaceda 
# Date:   27 June 2019
# Description: Creating documents and querying
#===========================================
#importing necessary modules 
from pymongo import MongoClient
import pprint
import datetime
#connececting to our mongoDB instance
client = MongoClient('localhost',27017)
#selecting our database
db=client.web335
#creating user
user ={
    "firstName":"Elizabeth",
    "lastName":"Ryan",
    "email":"eRyan@email.com",
    "employee_id":"7683994",
    "date_created":datetime.datetime.utcnow()
}
#inserting the new user
user_id=db.users.insert_one(user).inserted_id
#printing the user
print(user_id)
#quering the new user who was inserted 
pprint.pprint(db.users.find_one({"employee_id":"7683994"}))