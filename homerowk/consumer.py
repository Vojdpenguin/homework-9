import logging
from initialize_db import initialize_db
from models import Contact
import pika

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(contact):
    logging.info(f"Відправка email на {contact.email}")
    contact.sent = True
    contact.save()
    logging.info(f"Статус повідомлення для {contact.email} оновлено як 'відправлено'")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    logging.info(f"Отримано повідомлення з id контакту: {contact_id}")
    contact = Contact.objects(id=contact_id).first()

    if contact:
        if not contact.sent:
            logging.info(f"Контакт знайдено: {contact.full_name}, email: {contact.email}. Починається відправка.")
            send_email(contact)
        else:
            logging.info(f"Email вже відправлено для контакту: {contact.full_name}, email: {contact.email}")
    else:
        logging.warning(f"Контакт з id {contact_id} не знайдено")


if __name__ == '__main__':
    logging.info("Ініціалізація бази даних...")
    initialize_db()

    logging.info("Підключення до RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    logging.info("Очікування повідомлень. Для виходу натисніть CTRL+C")
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
