# MongoDB to Kafka Example

This code detects new documents by querying the MongoDB database and sends these documents as a JSON message to an Apache Kafka topic (topic).

Then an application that consumes messages from Kafka is also provided.

## Runing

1. Create Docker images to run your developed applications:

```shell
docker build -t producer-image -f Dockerfile-producer .
docker build -t consumer-image -f Dockerfile-consumer .
```

2. Use the following command to start services with Docker Compose:

```shell
docker-compose up
```

This command will start MongoDB, Kafka, producer (producer) and three consumer (consumer) Docker containers.

3. The producer application will query MongoDB every 10 seconds and send new documents to Kafka as a JSON message. Consumer (consumer) applications will print messages from Kafka to the console.

## Licence

You can refer to [LICENSE](LICENSE) file for license details of this project.

## Contribute

To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of Conduct

You can refer to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for the code of conduct for this project.