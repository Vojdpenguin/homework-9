from connect import connect_to_db
from models import save_data, Quote, Author


def search(command):
    command_parts = command.split(':', 1)
    if len(command_parts) != 2:
        print("Неправильний формат команди. Спробуйте ще раз.")
        return True

    action = command_parts[0].strip()
    value = command_parts[1].strip()

    if action == "name":
        author = Author.objects(fullname=value).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(f"{quote.quote} - {author.fullname}")
        else:
            print("Автор не знайдений.")

    elif action == "tag":
        quotes = Quote.objects(tags=value)
        for quote in quotes:
            print(quote.quote)

    elif action == "tags":
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)

    elif action == "exit":
        print("Завершення...")
        return False

    else:
        print("Невідома команда.")

    return True

if __name__ == "__main__":
    connect_to_db()
    # save_data()
    while True:
        command = input("Введіть команду: ").strip()
        if not search(command):
            break
