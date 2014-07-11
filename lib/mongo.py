from pymongo import MongoClient

client = MongoClient('eagle', 27017)

db = client['fullstack-dev']

collection = db.test_collection



# post = {"author": "Harley",
#         "text": "Hello World!",
#         "tags": ["mongodb", "python", "random crap"]
#         }

# post_id = collection.insert(post)
# print post_id
