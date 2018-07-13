import time

from confluent_kafka import Consumer

from settings import KAFKA_SERVER, KAFKA_TOPIC

FLUSH_INTERVAL = 5
BATCH_SIZE = 100
GROUP_ID = 'group-id'

kc = Consumer({
    'bootstrap.servers': KAFKA_SERVER,
    'group.id': GROUP_ID,
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    },
})

kc.subscribe([KAFKA_TOPIC])
running = True


def process_messages(batch_msgs):
    print('messages processed: {}'.format(len(batch_msgs)))
    for msg in batch_msgs:
        print('message: "{}" offset: {}'.format(msg.value().decode("utf-8"), msg.offset()))


print('Kafka consumer started!')
while running:
    msgs = kc.consume(num_messages=BATCH_SIZE)
    process_messages(msgs)
    print('\nnext batch in {} seconds...'.format(FLUSH_INTERVAL))
    time.sleep(FLUSH_INTERVAL)
kc.close()
