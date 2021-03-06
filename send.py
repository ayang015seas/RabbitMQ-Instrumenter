# send.py sends a message to a RabbitMQ server
# In our case, we generate a random number and send it each time

import pika
#from random import seed
import random

#seed(1)
r1 = random.randint(0, 10)

# Connect to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Send message
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
	routing_key='hello',
	body= str(3.0))

print(" Sent Hello World")
#print(random())
print(r1)

connection.close()

