from confluent_kafka import Consumer

kc = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test',
})

kc.subscribe(['test'])
running = True

def process_messages(batch_msgs):
    print('messages processed:{}'.format(len(batch_msgs)))
    for msg in batch_msgs:
	    print(msg.value())

while running:
    batch_size=10
    msgs = kc.consume(num_messages=10, timeout=10)
    process_messages(msgs)
c.close()