#!/usr/bin/env python
import time
import sys

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

# create an exchange
channel.exchange_declare(exchange="logs", exchange_type="fanout")

try:
    while True:
        message = " ".join(sys.argv[1:]) or "info: Hello World!"
        channel.basic_publish(exchange="logs", routing_key="", body=message)
        print(f" [x] Sent {message}")
        time.sleep(1)
finally:
    connection.close()
