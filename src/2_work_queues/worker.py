import sys
import time
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

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(1)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="task_queue", on_message_callback=callback)

channel.start_consuming()
