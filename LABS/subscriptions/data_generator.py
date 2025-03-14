from uuid import uuid4
from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package
import random
from faker import Faker
import json
import time
import argparse

#######################
#
# Create an ArgumentParser object
# Optional number of events
# Optional filename to write benchmark to
#
#########################

parser = argparse.ArgumentParser(description='This script generates a configurable load on the database') 
parser.add_argument('-n', '--number', required=False, default=100, help='Optional: Integer-- Number of Events to Append')
parser.add_argument('-f', '--file', required=False, help='Optional: String -- Filename to write results to')

args = parser.parse_args() 

print('Number of Events:', args.number)

if args.file:
    print(f'Writing to {args.file}')

loop_size = int(args.number)
#######################################################
#
# Step 1. Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

#######################################################
#
# Step 2. Create a function that returns Events
#
#######################################################

fake = Faker()


# Random integer between 1 and 10 (inclusive)
# random_int = random.randint(0, 9)
#print(random_int)




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
    country_list = ["CAN", "USA", "MEX"]
    country = random.choice(country_list)
    random_int = random.randint(0, 9)
    stream_name = f"{country}-{random_int}"
    return stream_name





start_time = time.time()

x = range(loop_size)

for n in x:
    event = event_creator()
    my_stream = (stream_name_generator())
    event_stream = my_stream        # Define the stream name where the event will be appended
    client.append_to_stream(             # Append the event to a stream
        event_stream,                    # Name of the stream to append the event to
        events=[event],              # The event to append (in a list)
        current_version=StreamState.ANY  # Set to append regardless of the current stream state (you can ignore this for now)
    )

end_time = time.time()

execution_time = end_time - start_time

print("Execution time:", execution_time)    

if args.file:
    with open(args.file, "a") as f:
        f.write(f'Execution time:, {execution_time}\n')

client.close() 