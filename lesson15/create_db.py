import sqlite3

# Устанавливаем соединение с базой данных.
# Если файла 'anketa.db' не существует, он будет создан.
conn = sqlite3.connect('anketa.db')

# Создаем "курсор" - это специальный объект,
# который позволяет делать запросы к базе данных.
cursor = conn.cursor()

# Создаем таблицу 'anketa' с колонками для наших вопросов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS anketa (
        id INTEGER PRIMARY KEY,
        user_id INTEGER UNIQUE,
        age INTEGER,
        genre TEXT,
        movie TEXT
    )
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("База данных и таблица 'anketa' успешно созданы.")