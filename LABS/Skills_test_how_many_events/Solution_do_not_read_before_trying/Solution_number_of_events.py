from esdbclient import EventStoreDBClient, NewEvent, StreamState

#######################################################
#
# Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

#######################################################
#
# One way to get all the events present in the database
# Is to read the all stream and count events
# Note that clients have a different method for 
# reading the all stream vs reading a stream
# In python client.get_stream("<Stream Name>") will return
# all events in a named stream
# client.read_all(<options>) will return events in 
# the $all stream 
#
#######################################################

events = client.read_all(
    commit_position=0,
    limit=500,
)

########################################################
# The events object is a python iterator, unlike a list
# where you could call len(events) you have to iterate
# with a counter
#
#########################################################
length = sum(1 for _ in events)
print(length)  

client.close()