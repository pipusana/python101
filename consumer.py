import pika
import sys
import time
from rabbitmq import RabbitMQ

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

comsumer = RabbitMQ()
comsumer.connect_to_queue()
comsumer.consume(callback)
