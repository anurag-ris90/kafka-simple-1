# kafka-simple-1

Note: This is a practice project.
(source: https://www.youtube.com/watch?v=Ydts27Qa8H0)

## Steps:  

-> Run the docker compose file (docker-compose.yml) using the gui button in the IDE or the below command.

`docker-compose up`
or 
`docker-compose up -d`

- This spins two containers, kafka and zookeeper, with ports '9092' and '2181' of the docker host/engine (local computer) mapped to the respective ports in the individual containers.
- So even though the kafka and zookeeper servers are running in the isolated containers; any application/programme we run in the local system then may connect to `localhost:9092` to actually connect to the kafka server running on the same port but inside the container.
- The kafka server itself connects to the zookeeper server via the mapping `KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181` defined in the environment variables of the kafka container, where `zookeeper` is the host name which contains the zookeeper service (introspection: Alternatively we can let the kafka container find the zookeeper server/host by using `--link` depending on our requirement; this creates an entry in `/etc/hosts` in the kafka container).

-> Now as the kafka cluster is ready (zookeeper only to manage the cluster), we will make our producer and consumer applications. Follow below to see how to run them in an active console and how to create python application for them.

### Using console

-> Identify the kafka container id (`docker ps`) and start an interactive terminal session (`docker exec -it <kafka_container_id> /bin/bash`).

-> Locate Kafka binaries (`cd /opt/kafka/bin`).

-> Create a topic:

`./kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`


- We can set the number of partitions and replication factor using `--partition` and `--replication-factor` while creating the topic and also while altering an existing topic. In the `--create` command if don't provide any of these then kafka uses the default value i.e. 1
- Some other kafka topics command:

`./kafka-topics.sh --create --topic <topic_name> --bootstrap-server <broker_address> --partitions 2`

`./kafka-topics.sh --alter --topic <topic_name> --bootstrap-server <broker_address> --replication-factor 3`

`./kafka-topics.sh --list --bootstrap-server <broker_address>`

`./kafka-topics.sh --describe --bootstrap-server <broker_address>`

`./kafka-topics.sh --describe --bootstrap-server <broker_address> --topic <topic_name>`

`./kafka-topics.sh --help`

-> Run Kafka Producer

`./kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092`

-> Run Kafka Consumer

`./kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092 --from-beginning`
