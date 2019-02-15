from mongobox import MongoBox
import time


# Start up MongoDB with user permissions.
# In a real deployment we would simply connect to an existing,
# separately managed MongoDB deployment.

box = MongoBox(port=27017)
box.start()
client = box.client()

while True:
    time.sleep(1)
