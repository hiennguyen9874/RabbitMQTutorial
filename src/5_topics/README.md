# RabbitMQ tutorial - Topics

- Topic exchange
  - Messages sent to a topic exchange can't have an arbitrary routing_key - it must be a list of words, delimited by dots
  - A message sent with a particular routing key will be delivered to all the queues that are bound with a matching binding key. However there are two important special cases for binding keys
    - \* (star) can substitute for exactly one word.
    - \# (hash) can substitute for zero or more words.
