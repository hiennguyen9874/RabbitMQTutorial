# RabbitMQ tutorial - Remote procedure call (RPC)

- Run a function on a remote computer and wait for the result
- RPC over RabbitMQ is easy, a client sends a request message and a server replies with a response message
- In order to receive a response the client needs to send a 'callback' queue address with the request
