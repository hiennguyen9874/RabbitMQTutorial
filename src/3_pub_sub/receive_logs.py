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

channel.exchange_declare(exchange="logs", exchange_type="fanout")

# create a queue with a random name. delete consumer when connection is closed
result = channel.queue_declare(queue="", exclusive=True)

# result.method.queue contains a random queue name
queue_name = result.method.queue

# Create binding, logs exchange will append messages to our queue
channel.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
