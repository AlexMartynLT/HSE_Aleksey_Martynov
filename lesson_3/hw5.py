import json
import csv

# Шаг 1: Читаем ИНН из файла traders.txt
# Открываем файл с ИНН и читаем строки, убираем лишние пробелы и пустые строки
with open("traders.txt", "r", encoding="utf-8") as inn_file:
    inn_list = [line.strip() for line in inn_file if line.strip()]

# Шаг 2: Загружаем данные из файла traders.json
# Открываем JSON-файл и загружаем список организаций в переменную data
with open("traders.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Шаг 3: Ищем организации по ИНН и сохраняем нужную информацию
# Создаем пустой список, куда будем добавлять подходящие записи
result = []

for inn in inn_list:
    for org in data:
        # Сравниваем ИНН из файла с ИНН из JSON (ключ "inn" с маленькой буквы)
        if str(org.get("inn", "")).strip() == inn:
            # Добавляем в список словарь с нужной информацией
            result.append({
                "ИНН": inn,
                "ОГРН": org.get("ogrn", "Не найден"),
                "Адрес": org.get("address", "Не найден")
            })
            break  # Прекращаем поиск после первого совпадения

# Шаг 4: Записываем результат в файл traders.csv
# Открываем CSV-файл на запись и сохраняем туда результат
with open("traders.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["ИНН", "ОГРН", "Адрес"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Пишем заголовки столбцов
    for row in result:
        writer.writerow(row)  # Записываем каждую строку

# Печатаем сообщение об успешном завершении
print("Готово! Данные успешно записаны в traders.csv.")
