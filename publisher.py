import pika
import sys
from rabbitmq import RabbitMQ

publisher = RabbitMQ()
publisher.connect_to_queue()
publisher.publish_to_queue('Hello world')
publisher.close()