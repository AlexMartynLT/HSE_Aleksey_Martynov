"""
Программа создает json файл с данными по динамике потребительских цен по регионам из файла xlsx
"""
import json
import os
import requests
import openpyxl


class ParserCBRF:
    """
    Класс для загрузки и парсинга данных о приросте потребительских цен
    с сайта Центрального банка России.
    """

    def __init__(self, url: str, output_filename: str = 'consumer_prices.json'):
        """
        Инициализирует парсер с заданным URL и именем выходного файла.

        :param url: URL для скачивания XLSX файла.
        :param output_filename: Имя файла для сохранения данных в формате JSON.
        """
        self._url = url
        self._output_filename = output_filename
        self._data = {}

    def _download_file(self) -> str | None:
        """
        Приватный метод для скачивания файла по URL, имитируя браузер.

        :return: Путь к скачанному файлу или None в случае ошибки.
        """
        # Заголовок User-Agent, чтобы сервер не блокировал наш запрос (ошибка 403)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            print(f"Начинаю скачивание файла с {self._url}...")
            response = requests.get(self._url, headers=headers)
            response.raise_for_status()  # Проверка на ошибки HTTP (4xx или 5xx)

            file_path = 'reg_cpd.xlsx'
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Файл успешно скачан и сохранен как {file_path}")
            return file_path
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при скачивании файла: {e}")
            return None

    def _parse_file(self, file_path: str) -> None:
        """
        Приватный метод для парсинга XLSX файла.

        :param file_path: Путь к XLSX файлу.
        """
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.worksheets[0]

            # Читаем заголовки (кварталы), пропуская первую ячейку.
            # Принудительно преобразуем в строку, чтобы избежать проблем с JSON.
            header = [str(cell.value) for cell in sheet[1][1:] if cell.value is not None]

            # Итерируемся по строкам с данными, начиная со второй
            for row in sheet.iter_rows(min_row=2, values_only=True):
                region_name = row[0]

                # Пропускаем строки без названия региона
                if not region_name:
                    continue

                self._data[region_name] = {}

                # Сопоставляем данные с заголовками
                for idx, value in enumerate(row[1:]):
                    if idx < len(header):
                        quarter_key = header[idx]
                        self._data[region_name][quarter_key] = value

        except Exception as e:
            print(f"Ошибка при парсинге файла: {e}")
            # Очищаем данные в случае ошибки парсинга, чтобы не записать неполный результат
            self._data = {}

    def _serialize_to_json(self) -> None:
        """
        Приватный метод для сериализации данных в JSON и сохранения в файл.
        """
        if not self._data:
            print("Нет данных для сохранения. Сериализация отменена.")
            return

        try:
            with open(self._output_filename, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в файл {self._output_filename}")
        except IOError as e:
            print(f"Ошибка при сохранении данных в JSON: {e}")

    @staticmethod
    def _deserialize_from_json(filename: str) -> dict:
        """
        Статический метод для десериализации данных из JSON файла.

        :param filename: Имя JSON файла.
        :return: Словарь с данными.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Ошибка при чтении данных из JSON: {e}")
            return {}

    def start(self) -> bool:
        """
        Публичный метод для запуска всего процесса.
        :return: True в случае успеха, False в случае неудачи.
        """
        file_path = self._download_file()
        if not file_path:
            return False

        try:
            self._parse_file(file_path)
            self._serialize_to_json()
        finally:
            # Блок finally гарантирует, что временный файл будет удален,
            # даже если на этапе парсинга или сериализации возникнет ошибка.
            os.remove(file_path)
            print(f"Временный файл {file_path} удален.")

        # Если self._data не пустой, значит парсинг и сериализация прошли успешно
        return bool(self._data)


if __name__ == '__main__':
    # URL файла с данными
    cbr_url = "https://cbr.ru/Content/Document/File/175223/reg_cpd.xlsx"

    # Создаем экземпляр парсера
    parser = ParserCBRF(url=cbr_url)

    # Запускаем процесс и сохраняем результат выполнения
    success = parser.start()

    # Проверяем десериализацию только в случае успешного завершения парсера
    if success:
        print("\n--- Проверка десериализации ---")
        data = ParserCBRF._deserialize_from_json('consumer_prices.json')
        if data:
            first_region_name = next(iter(data))
            print(f"Пример десериализованных данных для '{first_region_name}':")
            # Выводим первые 5 записей для наглядности
            for key, value in list(data[first_region_name].items())[:5]:
                print(f"  {key}: {value}")
    else:
        print("\nОсновная задача не была выполнена. Проверка десериализации пропущена.")