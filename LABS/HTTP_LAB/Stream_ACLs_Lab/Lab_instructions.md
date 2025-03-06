# Lab Modify Access Control List for a Stream

The ACL for a stream is stored in a metadata stream. This stream is the stream name prepended with "$$"

So the stream "mystream" has permissions managed in the system stream "$$mystream"

In this lab you will run some commands that use the http api to do the following.

1. Set permissions on a stream
2. Create the stream by appending an event
3. Verify that users not on the ACL can not access the stream.

Requirements:

This Lab requires a cluster running in secure mode. Secure mode requires ssl certificates. Typically these are signed by a CA, but for development purposes you can start a cluster in dev mode by passing "--dev" on the command line. The cluster startup script is provided for you.

This lab also requires that nodejs and npm are installed.

The tool httpyac is used to send requests the the http endpoints on the server.

httpyac was chosen because unlike curl, where the command line can get somewhat complicated, and additional files might be referenced for the post data, httpyac allows the complete http request, and the post data to be specified by a single file. For training purposes this is an approach that is less error prone.

## Step 1

Start a single node cluster, using "--dev" mode by running the ```start_secure_cluster.sh``` command.

## Step 2

Verify basic functionality by writing an event as the admin user, and reading it back.

```httpyac -a 01_write_test.http```

```httpyac -a 02_read_test.http```

If either of those commands fail, follow the following steps to debug.

1. Verify the cluster is running by checking the webui (note your browser will display an "insecure page warning due to the self signed certificate, click on advanced to ignore that warning)

Username: password
adnin   : changeit

2. If the cluster is not running, run the ```start_secure_cluster.sh``` script again. Report any errors to the instructor.

## Step 3

List the users of the cluster by running.

```httpyac -a  Get_user_data.http | grep loginName```

The output should be

```
"loginName": "admin",
"loginName": "ops",

```
Showing that the only two users configured for the cluster are admin and ops.

## Step 4

Secure a stream named "secure_stream" and only allow the user "audit" to access it.

```  httpyac -a update_acl.http ```

Verify the change has taken place by checking the stream browser in the webui

## Step 5

Add the audit user to the cluster

httpyac -a new_user.http

Verify by checking the admin tab on the webui

## Step 6

Try to write to the stream as the user audit.

```
httpyac -a write_as_audit_user.http

```

## Step 7

Try to write to the stream as a user other than "audit"

```
httpyac -a write_as_non_audit_user.http
```

## Congratulations you have secured a stream !!!