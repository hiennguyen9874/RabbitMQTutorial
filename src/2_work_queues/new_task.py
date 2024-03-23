import sys
import pika
import time

credentials = pika.PlainCredentials("admin", "mypass")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port="5672",
        credentials=credentials,
    )
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

try:
    while True:
        message = " ".join(sys.argv[1:]) or "Hello World!"
        channel.basic_publish(
            exchange="",
            routing_key="task_queue",
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(f" [x] Sent {message}")

        time.sleep(2)
finally:
    connection.close()
