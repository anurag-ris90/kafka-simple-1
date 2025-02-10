from kafka import KafkaProducer
from kafka.errors import KafkaError

import json

# Define Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce a message
future = producer.send('test-topic', 'shit')
try:
    record_metadata = future.get(timeout=10)
except KafkaError as e:
    print(f"Error sending message: {e}")
finally:
    producer.close()

# # Define Kafka producer
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )
#
# # Produce messages to different partitions
# for i in range(10):
#     partition = i % 3  # Distribute messages across 3 partitions
#     message = {'key': f'value-{i}', 'partition': partition}
#     producer.send('test-topic', value=message, partition=partition)
#
# # Flush and close the producer
# producer.flush()
# producer.close()
