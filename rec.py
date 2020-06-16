#!/usr/bin/env python
import pika
import _thread
from flask import Flask
from prometheus_client import start_http_server, Summary
import random
import time

from prometheus_client import Counter
c = Counter('my_failures', 'Description of counter')


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

rabbits = 0

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    global rabbits
    c.inc()
    rabbits += 1


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    channel.start_consuming()
    print("Server Start")
    # Generate some requests.
    while True:
        process_request(random.random())


# app = Flask(__name__)
# @app.route('/')
# def hello_world():
# 	return "Hello world!"

print("Flask app up!")

print(' [*] Waiting for messages. To exit press CTRL+C')

# channel.start_consuming()

# try:
# 	_thread.start_new_thread(channel.start_consuming())
# except:
# 	print("Error, thread fail")
# channel.start_consuming()


print("hit bottom")