Cluster started with,

docker run --name esdb-node -it -e HOME=/tmp -p 2113:2113 docker.eventstore.com/eventstore/eventstoredb-ee --insecure
--run-projections=All --enable-atom-pub-over-http