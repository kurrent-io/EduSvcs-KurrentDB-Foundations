from esdbclient import EventStoreDBClient, NewEvent, StreamState

#######################################################
#
# Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")


# YOUR CODE GOES HERE




##############
#
# Remember to close the client
#
###############

client.close()