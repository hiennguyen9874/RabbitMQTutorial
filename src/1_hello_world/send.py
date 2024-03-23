#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials("admin", "mypass")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port="5672",
        credentials=credentials,
    )
)
channel = connection.channel()

# create a hello queue
channel.queue_declare(queue="hello")

channel.basic_publish(
    exchange="",  # default exchange
    routing_key="hello",
    body="Hello World!",
)
print(" [x] Sent 'Hello World!'")
