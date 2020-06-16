# RabbitMQ-Instrumenter
Take in metrics from RabbitMQ, Expose in prometheus-friendly format.
In response to a requirement to take in metrics from RabbitMQ and display them to prometheus, we created this adapter.
Since there is no direct link from rabbitMQ to prometheus, we need some middleware. In our setup, our rabbitMQ messages are processed 
by a Python server, and then those metrics are aggregated on the server to be displayed via a prometheus endpoint. 

# Usage 
In our setup, we assume that RabbitMQ is already installed and running on localhost. If that isn't the case, instructions for that are 
here: https://www.rabbitmq.com/download.html

After RabbitMQ is running on localhost, we can start up the middleware server using:
python3 rec.py

To send messages to be interpreted by prometheus, we run the script:
python3 send.py

To visit the prometheus endpoint for metrics, go to localhost:8000

Further updates coming along. 
