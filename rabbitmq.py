import pika

class RabbitMQ():
  def __init__(self):
    self.queue_name = 'jimmie'

  def connect_to_queue(self):
    self.connection = pika.BlockingConnection(
          pika.ConnectionParameters(
            host='localhost',
            port=int(4672), 
            credentials=pika.PlainCredentials(
              'user',
              'password',
            )
        )
      )
    self.channel = self.connection.channel()

  def close(self):
        self.connection.close()

  def publish_to_queue(self, message):
      if self.connection.is_closed:
          self.connect_to_queue()

      self.channel.basic_publish(
          exchange='',
          routing_key=self.queue_name, 
          body=message,
          properties=pika.BasicProperties(
              delivery_mode = 2, # make message persistent
          )
      )
      print(" [x] Sent To Queue: " + str(message)+ " | Queue name: "+ self.queue_name)

  def consume(self, callback):
    try:
       print(' [*] Waiting for messages. To exit press CTRL+C')
       self.channel.basic_consume(consumer_callback=callback, queue=self.queue_name)
       self.channel.start_consuming()
    except KeyboardInterrupt:
      pass
