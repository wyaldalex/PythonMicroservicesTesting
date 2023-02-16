from confluent_kafka import Consumer

consumer = Consumer ({
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'testgrouppyth',
    'auto.offset.reset': 'earliest'

})

consumer.subscribe(['testerpyth'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print("Received message: {}".format(msg.error()))

