# consume_clients.py (à placer dans l’API Produits)

import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"📥 Message reçu : {method.routing_key} → {message}")
    # Ici tu peux, par exemple, enregistrer les nouveaux clients dans un cache local ou un fichier

def main():
    print("🎧 En attente des événements RabbitMQ (clients.created, clients.updated)...")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='events', exchange_type='topic')
    queue_name = 'products_listen_clients'
    channel.queue_declare(queue=queue_name, durable=True)

    channel.queue_bind(exchange='events', queue=queue_name, routing_key='clients.created')
    channel.queue_bind(exchange='events', queue=queue_name, routing_key='clients.updated')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()
