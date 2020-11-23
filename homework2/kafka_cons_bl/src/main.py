from kafka import KafkaConsumer
from processor import Processor
bootstrap_servers = ['localhost:9092']
topicName = 'topicblbtcusdt'

consumer = KafkaConsumer (topicName,
                          group_id ='group1',
                          bootstrap_servers =bootstrap_servers,
                          auto_offset_reset='earlies' )

processor = Processor()
def consume():
    for msg in consumer:
        processor.add_msg(msg.value)
        processor.print_msg()


if __name__ == "__main__":
    consume()