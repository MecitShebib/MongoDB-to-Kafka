from kafka import KafkaConsumer

# Kafka bağlantısı ve yapılandırması
consumer = KafkaConsumer('X_topic', bootstrap_servers='localhost:9092')

# Mesajları tüket
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
