from esdbclient import EventStoreDBClient, NewEvent, StreamState
import json 
import os

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

#########
# Subscribe to the stream 
# that has all events in streams 
# that start with "CAN"
#########

stream_name = "$ce-CAN"


##############
# Catchup subscriptions start at a defined stream position
# The assumption is that the logic stores the stream position
# of last processed event
# and continues from there
# In this case a file will store stream position 
# along with the data processed from the stream
#############

#################
# Read the file to see if a checkpoint is available
# file format is
# checkpoint, username
# if the file exists
# read the last line, 
# split on comma and use that as stream_position
###############


file_path = 'Canada_userlist.txt'

if os.path.exists(file_path):
    print(f"File exists at: {file_path}")
    with open('Canada_userlist.txt',"r") as f:
        for line in f:
            pass
        last_line = line
        our_stream_position = int(last_line.split(",")[0])
else:
    print(f"File does not exist at: {file_path}")
    our_stream_position = 0
  

print(f' Our stream position to "catchup" from is {our_stream_position}')
print('Enter ctrl-C twice in the terminal to stop')




############ 
# Create a catchup or self-managed subscription
# Here are the available options
# stream_name: str,
#     *,
#     stream_position: int | None = None,
#     from_end: bool = False,
#     resolve_links: bool = False,
#     include_caught_up: bool = False,
#     timeout: float | None = None,
#     credentials: CallCredentials | None = None
####################

client.subscribe_to_stream

subscription = client.subscribe_to_stream(stream_name, 
    stream_position = our_stream_position,
    resolve_links= True
)

########
# The event handler is going to 
# build a list of user names per country
# Note that we store the stream_position in the file as well
# Caution, opening and closing a file per event may not
# be best practices for production code
########



def handle_event(event):
    # convert event JSON to python dictionary
    json_string = json.loads(event.data) 

    # Extract the stream position and user name
    event_id_name = (f"{event.link.stream_position},{json_string['name']}")

    # Open our user list file
    f = open("Canada_userlist.txt", "a")
    print(f'Writing {event_id_name} to file')
    f.write(event_id_name + "\n")
    f.close()

  
for event in subscription:
    #############
    # Uncomment the lines below to view additional information
    ############
   
    # print(f"received event: {event.stream_position} {event.type}")
    # print(event.commit_position)
    # print(event.stream_position)
    # print(event.link.stream_position)
    # event_id_name = (f"{event.link.stream_position},{json_string['name']}")
    # print(event_id_name)
   
    handle_event(event)
    

client.close()
