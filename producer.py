from confluent_kafka import Producer

from settings import KAFKA_SERVER, KAFKA_TOPIC

MESSAGE_COUNT = 1000

p = Producer({'bootstrap.servers': KAFKA_SERVER})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message "{}" delivered to "{}" [{}]'.format(msg.value().decode("utf-8"), msg.topic(), msg.partition()))


print('Kafka producer started!')
for i in range(MESSAGE_COUNT):
    message = 'hello world - {}'.format(i + 1)
    p.produce(KAFKA_TOPIC, value=message, callback=delivery_report)
    print('{}/{} - {}'.format(i + 1, MESSAGE_COUNT, message))
p.flush()
