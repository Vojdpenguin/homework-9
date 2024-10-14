import mongoengine as me
import configparser

# Читання даних із файлу конфігурації
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

try:
    def connect_to_db():
        # Підключення до MongoDB Atlas
        me.connect(
            host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Clust""",
            ssl=True)
        print("Підключення до бази даних успішне!")
except Exception as e:
    print(f"Помилка підключення до бази даних: {e}")
