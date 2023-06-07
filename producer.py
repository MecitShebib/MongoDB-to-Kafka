import time
from kafka import KafkaProducer
from pymongo import MongoClient
import json

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Kafka bağlantısı ve yapılandırması
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'X_topic'

# Son işlem zamanı
last_processed_time = None

while True:
    # Son işlem zamanını al
    last_processed_time = time.time() if last_processed_time is None else last_processed_time
    
    # Yeni dökümanları sorgula
    new_documents = collection.find({"timestamp": {"$gt": last_processed_time}})
    
    # Her yeni döküman için işlem yap
    for document in new_documents:
        # JSON mesajını oluştur
        message = {
            'id': str(document['_id']),
            'data': document['data']
        }
        
        # JSON mesajını Kafka'ya gönder
        producer.send(topic, json.dumps(message).encode('utf-8'))
        print(f"Message sent: {message}")
    
    # Son işlem zamanını güncelle
    last_processed_time = time.time()
    
    # 10 saniye bekle
    time.sleep(10)
