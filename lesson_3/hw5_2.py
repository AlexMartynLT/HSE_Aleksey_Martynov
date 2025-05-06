import json  # Модуль для работы с JSON
import re    # Модуль для регулярных выражений


# Функция для поиска email-адресов в тексте
def extract_emails(text):
    # Регулярное выражение для поиска email-адресов
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Ищем все email-адреса и возвращаем как список
    return re.findall(email_pattern, text)


# Загружаем JSON-файл с сообщениями
with open("1000_efrsb_messages.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем содержимое в переменную

emails_by_inn = {}  # Словарь для хранения email по ИНН

# Обрабатываем каждое сообщение
for message in data:
    # Получаем ИНН публикующего
    inn = message.get("publisher_inn")

    # Преобразуем всё сообщение в одну строку, чтобы искать email в любом месте
    full_text = json.dumps(message, ensure_ascii=False)

    # Ищем email-адреса
    emails = extract_emails(full_text)

    # Добавляем ИНН в словарь, даже если email нет
    emails_by_inn[inn] = set(emails) if emails else set()

# Преобразуем множества в списки, чтобы сохранить в JSON
emails_by_inn_serializable = {
    inn: list(emails) for inn, emails in emails_by_inn.items()
}

# Сохраняем результат в файл emails.json
with open("emails.json", "w", encoding="utf-8") as output_file:
    json.dump(
        emails_by_inn_serializable, output_file,
        ensure_ascii=False, indent=4
    )

# Выводим, сколько ИНН было обработано
print(f"Обработано ИНН: {len(emails_by_inn)}")
