from uuid import uuid4
from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package
import random
from faker import Faker
import json
import time
import argparse
import hashlib

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

random_int = random.randint(0, 100)
#print(random_int)

fake = Faker()

hash_value = (hashlib.md5(str(random_int).encode('utf-8')).hexdigest())

with open("hashed_solution.txt", "w") as file:
    file.write(hash_value)
file.close()    

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

def stream_name_generator():
    country = fake.country_code('alpha-3')
    stream_name = f"{country}-{00}"
    return stream_name


x = range(random_int)

for n in x:
    event = event_creator()
    my_stream = (stream_name_generator())
    event_stream = my_stream        # Define the stream name where the event will be appended
    client.append_to_stream(             # Append the event to a stream
        event_stream,                    # Name of the stream to append the event to
        events=[event],              # The event to append (in a list)
        current_version=StreamState.ANY  # Set to append regardless of the current stream state (you can ignore this for now)
    )

print("\nTest Data Has been written\n")    

client.close()    