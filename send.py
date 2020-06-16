# send.py sends a message to a RabbitMQ server
# In our case, we generate a random number and send it each time

import pika
from random import seed
from random import random

seed(1)

# Connect to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Send message
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
	routing_key='hello',
	body= str(random())
	)

print(" Sent Hello World")

connection.close()

