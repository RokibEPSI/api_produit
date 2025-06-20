# consume_orders.py (à placer dans l’API Produits)

import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"📥 Message reçu : {method.routing_key} → {message}")
    # Exemple : ici tu pourrais décrémenter le stock des produits commandés
    # en fonction des IDs des produits dans le message

def main():
    print("🎧 En attente des événements RabbitMQ (orders.created)...")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='events', exchange_type='topic')
    queue_name = 'products_listen_orders'
    channel.queue_declare(queue=queue_name, durable=True)

    channel.queue_bind(exchange='events', queue=queue_name, routing_key='orders.created')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()
