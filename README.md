# POC Consume messages in batch using Kafka

## Setup kafka and zookeeper
```bash
brew install kafka
```

## Running the services
```bash
brew services start zookeeper
brew services start kafka
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