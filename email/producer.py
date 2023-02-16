from confluent_kafka import Producer

producer = Producer ({
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'testgrouppyth',
    'auto.offset.reset': 'earliest'

})

for x in range(10):
  producer.produce('testerpyth', "Random string {}".format(str(x)))

producer.flush()

