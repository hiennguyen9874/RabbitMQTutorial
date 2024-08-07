#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials("admin", "mypass")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port="5672",
        credentials=credentials,
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="direct_logs", routing_key=severity, body=message)
print(f" [x] Sent {severity}:{message}")
connection.close()
