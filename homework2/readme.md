## Kafka server config

bin/kafka-topics.sh --version

# add new line in file server.properties
```
listeners=PLAINTEXT://localhost:9092
```

/usr/lib/kafka/config




#go to kafka catalog

```
cd /usr/lib/kafka
```

# start kafka server
```
sudo bin/kafka-server-start.sh config/server.properties
```

# create topic 
```
bin/kafka-topics.sh --create     --zookeeper localhost:2181 \
     --replication-factor 1 \
     --partitions 2 \
     --topic topicblbtcusdt

```
#Push test messages to the topic via sh script 

```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topicblbtcusdt
```

#check kafka version

```
bin/kafka-topics.sh --version
```

## Nifi template

 Nifi template coud be found by the next path

```
homework2/nifi_template_bogdan_lesiv_kafka.xml

```
[a link to nifi template] (https://github.com/bohdanlesiv/GL-task/blob/master/homework2/nifi_template_bogdan_lesiv_kafka.xml)


## Kafka consumer 

Consumer for messages was created based on Python 3.7

In oreder to run the client next steps are mandatory

1. Create directory kafka_cons_bl
2. Inside the directory kafka_cons_bl create virtual env ven
3. Install the pakgs 
```
homework2/requirements.txt

```
[a link to requirements ] (https://github.com/bohdanlesiv/GL-task/blob/master/homework2/kafka_cons_bl/requirements.txt)

4. Upload the folder homework2\kafka_cons_bl\src with files main.py and processor.py

[a link to code] (https://github.com/bohdanlesiv/GL-task/tree/master/homework2/kafka_cons_bl/src)

In additional I have implemented message validation based on message schama see processor.py



