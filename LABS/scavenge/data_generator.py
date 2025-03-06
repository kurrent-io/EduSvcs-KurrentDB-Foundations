from uuid import uuid4
from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package
import random
from faker import Faker
import json
import time




#######################################################
#
# Step 1. Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS


##############
# Connection string to connect to insecure cluster
##############
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false") 



#######################################################
#
# A function that returns Events
#
#
#######################################################

fake = Faker()

def event_creator():
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "job": fake.job()
    }

    json_data = json.dumps(data)
    #print(type(json_data))

    new_event = NewEvent(
        id=uuid4(),
        type="TestEvent",
        data=json_data.encode('utf-8')
    )
    return new_event

############################
# A Function that returns stream names
############################


def stream_name_generator():
    country = fake.country_code('alpha-3')
    random_int = random.randint(0, 9)
    stream_name = f"{country}-{random_int}"
    return stream_name


################
# Generate events_lists containing 100 events
##############

events_list = []
for n in range(100):
    event = event_creator()
    events_list.append(event)

#####
# Generate list of 5 stream Names
######

stream_names = []
for n in range(5):
    stream_name = stream_name_generator()
    stream_names.append(stream_name)


#################
# SET STREAM metadata to have
# $maxCount of 2
# ############## 


########
# Define an Event to append to each streams metadata stream
########
new_event = NewEvent(
    type="set_count",
    data=b'{"$maxCount": 2}'
)   

#######
# Append the $maxCount setting in a loop of stream names list
# Note the $$<stream_name 
# this is the metadata stream
#######

for name in stream_names:
    client.append_to_stream(
        f"$${name}",
        events = [new_event],
        current_version = StreamState.ANY
    )



#######################
# For each stream name in list
# append the events in a batch
#######################

for name in stream_names:
    print(f"/writing to stream {name}")
    try:
        event_stream = name        # Define the stream name where the event will be appended
        client.append_to_stream(             # Append the event to a stream
        event_stream,                    # Name of the stream to append the event to
        events=events_list,              # The event to append (in a list)
        current_version=StreamState.ANY  # Set to append regardless of the current stream state (you can ignore this for now)
        )
    except:
        print("Timeout: sleep for 2 seconds and try again")
        time.sleep(2)
    



client.close() 