# RabbitMQ tutorial - Work Queues

- Work Queue: distribute time-consuming tasks among multiple workers
  - The main idea behind Work Queues: avoid doing a resource-intensive task immediately and having to wait for it to complete
  - We encapsulate a task as a message and send it to the queue
  - A worker process running in the background will pop the tasks and eventually execute the job
  - When you run many workers the tasks will be shared between them
