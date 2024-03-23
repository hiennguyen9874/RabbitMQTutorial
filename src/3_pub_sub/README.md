# RabbitMQ tutorial - Publish/Subscribe

- Deliver a message to multiple consumers (known as "publish/subscribe")

- The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue

- Producer can only send messages to an exchange

  - On one side it receives messages from producers and on the other side it pushes them to queues
  - Exchange must know exactly what to do with a message it receives
  - Fanout exchange: broadcasts all the messages it receives to all the queues it knows

- Temporary queues

  - We want to hear about all log messages, not just a subset of them
  - We're also interested only in currently flowing messages not in the old ones

- Bindings
  - We need to tell the exchange to send messages to our queue
  - That relationship between exchange and a queue is called a binding
