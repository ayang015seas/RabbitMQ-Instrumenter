# send.py sends a message to a RabbitMQ server
# In our case, we generate a random number and send it each time

import pika
#from random import seed
import random
import threading

#seed(1)
r1 = random.randint(0, 10)

# Connect to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Send message
def send():
	threading.Timer(2.0, send).start()
	r2 = random.randint(0, 10)
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='',
		routing_key='hello',
		body= str(r2))
	print("Sent")

send()

print("Finished Script")
#print(random())
print(r1)

# connection.close()

