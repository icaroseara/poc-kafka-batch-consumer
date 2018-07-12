from confluent_kafka import Producer

MESSAGE_COUNT = 1000

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for i in range(MESSAGE_COUNT):
    message = 'hello world - {}'.format(i)
    p.produce('test', value=message, callback=delivery_report)
    print('{}/{} - {}'.format(i, MESSAGE_COUNT,message))
p.flush(5)
