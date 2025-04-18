# -*- coding: utf-8 -*-
"""
hw_3_2.py

Интерактивный генератор «шапки» процессуального документа.
lesson_2_data.py должен лежать в той же папке.
"""

import os
import sys

# делаем так, чтобы Python точно увидел lesson_2_data.py рядом с этим скриптом
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

import lesson_2_data  # из вашего файла: respondents и courts :contentReference[oaicite:0]{index=0}

def generate_header(respondent: dict, plaintiff: dict) -> str:
    """
    Формирует шапку по данным:
      - plaintiff: {'full_name', 'inn', 'ogrn', 'address'}
      - respondent: {'short_name', 'inn', 'ogrn', 'address', 'case_number'}
    """
    case_number = respondent['case_number']
    court_code = case_number.split('-')[0]   # код до дефиса, например 'А40'

    court = lesson_2_data.courts.get(court_code)
    if court is None:
        raise ValueError(f"Суд с кодом {court_code!r} не найден.")

    return f"""\
В арбитражный суд {court['court_name'].lower()}
Адрес: {court['court_address']}

Истец: {plaintiff['full_name']}
ИНН {plaintiff['inn']} ОГРН(ИП) {plaintiff['ogrn']}
Адрес: {plaintiff['address']}

Ответчик: {respondent['short_name']}
ИНН {respondent['inn']} ОГРН(ИП) {respondent['ogrn']}
Адрес: {respondent['address']}

Номер дела {case_number}
"""

def main():
    # 1) Вводим данные истца
    print("=== Введите данные Истца ===")
    plaintiff = {
        'full_name': input("Полное имя: ").strip(),
        'inn':        input("ИНН: ").strip(),
        'ogrn':       input("ОГРН(ИП): ").strip(),
        'address':    input("Адрес: ").strip()
    }

    # Сколько ответчиков обработать?
    try:
        count = int(input("\nСколько ответчиков хотите ввести? "))
    except ValueError:
        count = 1

    for i in range(1, count + 1):
        print(f"\n=== Ответчик #{i} ===")
        respondent = {
            'short_name':  input("Короткое наименование: ").strip(),
            'inn':         input("ИНН: ").strip(),
            'ogrn':        input("ОГРН(ИП): ").strip(),
            'address':     input("Адрес: ").strip(),
            'case_number': input("Номер дела (например A40-12345/2023): ").strip()
        }

        # Генерируем и печатаем шапку
        try:
            header_text = generate_header(respondent, plaintiff)
        except Exception as e:
            print(f"Ошибка: {e}")
        else:
            print("\n--- Сгенерированная шапка ---")
            print(header_text)
            print("-" * 60)

if __name__ == "__main__":
    main()

