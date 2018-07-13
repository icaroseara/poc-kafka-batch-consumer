# POC Consume messages in batch using Kafka

## Prerequisites
- [Apache Kafka](http://kafka.apache.org)
- [Apache ZooKeeper](https://zookeeper.apache.org)
- [Python](https://www.python.org)

## Setup Kafka and ZooKeeper
```bash
brew install kafka
```

## Running the services
```bash
brew services start zookeeper
brew services start kafka
```

## Test if the Zookeeper server is really started
```bash
telnet localhost 2181
```

## Test if the Kafka server is really started
```bash
telnet localhost 9092
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Produce messages
```bash
python producer.py
```
## Consume messages in batch
```bash
python consumer.py
```

## Replay messages in a topic
```bash
kafka-run-class kafka.tools.ReplayLogProducer --broker-list localhost:9092 --inputtopic events.created
```