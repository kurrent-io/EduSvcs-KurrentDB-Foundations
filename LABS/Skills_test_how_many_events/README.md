# EventStoreDB Skills Test

Find the number of events present in the cluster.

## Purpose: 

In this lab you will write code to determine: 
1. How many events have been written

## Overview of the challenge

The python script `Generate_random_test_data.py` when ran will write 
a random number of events to EventStoreDB. The cluster connection will work for a local, unsecured cluster only. 

The events will be written to streams with the name

Country_Code-0

There are 249 "countries" in the ISO 3166-1 standard. 

So there is a 1/249 chance that each write will be the second write to the stream. 

Practically that means that number of events will not always equal number of streams. 

The challenge is be to determine the number of events that EventStoreDB contains after the `Generate_random_test_data.py` has been ran. 


## Running the challenge

### Step 1: 

Start with an **empty** EventStoreDB database. 

If running locally execute the following steps:
1. Stop your cluster
2. Delete your data directory
3. Restart your cluster


### Step 2: 
Run the data generator

If running in vscode you should be able to open the script, and use the run arrow. 

If running outside of vscode, then you would want to create a venv, and install the requirements in requirements.txt


### Step 3:
Verify the events have been written to your cluster by viewing the webui at 
http://localhost:2113

You should see streams with names similar to these, 
BHS-0
FJI-0
IRL-0
KOR-0

### Step 4:

Write some code to get the number of events written to the Cluster.

Challenge_number_of_events.py provides a template, 
but you are welcome to solve this any way you choose. 

When you think you have an answer, run tester.py to enter the count of events and see if you are correct.

If you have found the answer, congratulations you are done with the Lab.

If you had issues, see the notes section below, or view the Solution in the Solution directory.

**Note**
`tester.py` records the counts of events written by the last run of `Create_random_test_data.py``

If you are sure you are correct, and the test says you are wrong, this could be caused by the following: 

1. Running `Create_random_test_data.py` more than once
2. Not starting with an empty cluster

The solution is to clear your cluster's data directory, restart, and run the data generator and your solution in that order, and try the tester.py check again. 

