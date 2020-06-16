import pika
from random import seed
from random import random

seed(1)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
	routing_key='hello',
	body= str(random())
	)

print(" Sent Hello World")

connection.close()

