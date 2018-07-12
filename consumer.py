import time

from confluent_kafka import Consumer

kc = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group-identifier',
})

kc.subscribe(['events.created'])
running = True


def process_messages(batch_msgs):
    print('messages processed:{}'.format(len(batch_msgs)))
    for msg in batch_msgs:
        print(msg.value())


while running:
    msgs = kc.consume(num_messages=10)
    process_messages(msgs)
    print('\nthe next pull will happens in 10 seconds...')
    time.sleep(10)
kc.close()
