All of these examples inlcude a basic Authentication Header. 
The default username password of admin:changeit is used
The server is started with --dev mode which uses a self signed certificate
The .httpyac.json file in the base directory overrides strict certificate checking 

Docker command to start server for this demo

docker run --name esdb-node -it -e HOME=/tmp -p 2113:2113 docker.eventstore.com/eventstore/eventstoredb-ee --dev --run-projections=All --enable-atom-pub-over-http