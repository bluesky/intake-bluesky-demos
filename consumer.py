from pymongo import MongoClient
from bluesky.callbacks.zmq import RemoteDispatcher
from suitcase.mongo_normalized import Serializer

# This listens to a lightweight (0MQ-based) message bus for Documents
# and inserts them into MongoDB.

dispatcher = RemoteDispatcher('localhost:5578')

client = MongoClient('localhost:27017')
serializer = Serializer(client['mds'], client['assets'])
print(client.address)
dispatcher.subscribe(serializer)
dispatcher.start()
