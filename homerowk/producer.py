import logging
from initialize_db import initialize_db
from models import Contact
import faker

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_contacts(count):
    fake = faker.Faker()
    contacts = []
    for i in range(count):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            message_sent=False,
            additional_info=fake.text()
        )
        contact.save()
        contacts.append(contact)
        logging.info(f"Згенеровано контакт {i + 1}: {contact.full_name}, email: {contact.email}")
    return contacts


if __name__ == '__main__':
    logging.info("Ініціалізація бази даних...")
    initialize_db()

    logging.info("Генерація контактів...")
    generate_contacts(10)

    logging.info("Завершено.")
