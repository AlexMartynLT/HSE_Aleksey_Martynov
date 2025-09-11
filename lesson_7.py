# Импортируем класс datetime, чтобы удобно работать с датой и временем.
from datetime import datetime

# Объявляем класс CourtCase — он будет хранить данные по одному судебному делу.
class CourtCase:
    # Докстрока класса — кратко объясняем, что делает класс.
    """Класс, представляющий судебное дело с участниками, слушаниями и вердиктом."""

    # Конструктор — метод, который вызывается при создании экземпляра класса.
    def __init__(self, case_number, case_participants=None, listening_datetimes=None, is_finished=False, verdict=""):
        # case_number — обязательный параметр: строка с номером дела.
        # Если кто-то не передаст case_participants, мы не хотим использовать пустой список как значение по умолчанию,
        # потому что такое значение будет общим для всех экземпляров. Поэтому используем None и заменим его внутри.
        # Сохраняем номер дела в атрибут экземпляра.
        self.case_number = case_number

        # Если case_participants равен None, создаём новый пустой список; иначе используем переданный список.
        self.case_participants = [] if case_participants is None else list(case_participants)

        # Если listening_datetimes равен None, создаём новый пустой список; иначе используем переданный список.
        # Этот список будет хранить сведения о судебных слушаниях (например, даты и место).
        self.listening_datetimes = [] if listening_datetimes is None else list(listening_datetimes)

        # Флаг, показывающий, завершено ли дело; по умолчанию False (дело не завершено).
        self.is_finished = is_finished

        # Вердикт по делу — по умолчанию пустая строка.
        self.verdict = verdict

    # Метод для добавления участника в дело (например, ИНН или любое другое строковое обозначение).
    def add_participant(self, participant):
        # Комментарий: если участник уже есть в списке, ничего не делаем и возвращаем False.
        if participant in self.case_participants:
            # Возвращаем False, чтобы вызывающий код мог понять: участник уже был.
            return False
        # Добавляем нового участника в список.
        self.case_participants.append(participant)
        # Возвращаем True, чтобы показать, что добавление прошло успешно.
        return True

    # Метод для удаления участника из списка.
    def remove_participant(self, participant):
        # Если участника в списке нет, ничего не делаем и возвращаем False.
        if participant not in self.case_participants:
            return False
        # Убираем участника из списка.
        self.case_participants.remove(participant)
        # Возвращаем True — удаление успешно.
        return True

    # Метод для добавления судебного заседания в список listening_datetimes.
    # Параметр dt может быть объектом datetime или строкой вида "YYYY-MM-DD HH:MM" или ISO.
    # location и note — дополнительные сведения (по желанию).
    def set_a_listening_datetime(self, dt, location=None, note=None):
        # Попробуем преобразовать строку в объект datetime, если передали строку.
        if isinstance(dt, str):
            try:
                # Пытаемся распарсить строку в формате ISO или "YYYY-MM-DDTHH:MM:SS"
                parsed_dt = datetime.fromisoformat(dt)
            except ValueError:
                try:
                    # Если предыдущая попытка не удалась, пробуем формат "YYYY-MM-DD HH:MM"
                    parsed_dt = datetime.strptime(dt, "%Y-%m-%d %H:%M")
                except Exception:
                    # Если всё равно не получилось, оставляем dt как есть (строкой) — так тоже допустимо.
                    parsed_dt = dt
        elif isinstance(dt, datetime):
            # Если dt уже объект datetime, просто используем его.
            parsed_dt = dt
        else:
            # Если тип неожиданный, сохраняем как есть (может быть удобным для простых задач).
            parsed_dt = dt

        # Создаём структуру (словарь) для сведения о слушании: дата/время, место и заметка.
        hearing = {
            "datetime": parsed_dt,  # дата и время слушания (или строка, если не удалось распарсить)
            "location": location,   # место (например, "Зал №1")
            "note": note,           # дополнительная заметка
        }

        # Добавляем это слушание в список слушаний дела.
        self.listening_datetimes.append(hearing)

        # Возвращаем добавлённую структуру на всякий случай (удобно для тестов).
        return hearing

    # Метод вынесения решения по делу: устанавливаем verdict и помечаем дело как завершённое.
    def make_a_decision(self, verdict_text):
        # Записываем текст вердикта в атрибут экземпляра.
        self.verdict = verdict_text
        # Помечаем дело как завершённое.
        self.is_finished = True
        # Возвращаем True — операция выполнена успешно.
        return True

    # Удобный метод для строкового представления объекта — полезно при печати.
    def __str__(self):
        # Возвращаем краткую информацию: номер дела, количество участников, количество слушаний и статус.
        return (
            f"CourtCase(case_number={self.case_number!r}, "
            f"participants={len(self.case_participants)}, "
            f"hearings={len(self.listening_datetimes)}, "
            f"is_finished={self.is_finished})"
        )


# Пример использования класса:
if __name__ == "__main__":
    # Создаём экземпляр дела с номером (это обязательный параметр).
    case = CourtCase("А-123/2025")

    # Добавляем участников (например, по ИНН или просто по строкам).
    case.add_participant("7701234567")  # добавили участника 1
    case.add_participant("5009876543")  # добавили участника 2
    case.add_participant("7701234567")  # пробуем добавить дубликат — метод вернёт False и дубликат не добавится

    # Добавляем слушание — передаём строку с датой и временем.
    case.set_a_listening_datetime("2025-09-15 10:00", location="Зал №1", note="Предварительное слушание")

    # Добавляем слушание — передаём объект datetime напрямую.
    case.set_a_listening_datetime(datetime(2025, 10, 1, 14, 30), location="Зал №2")

    # Убираем участника
    case.remove_participant("5009876543")  # удалили второго участника

    # Вынесение решения по делу
    case.make_a_decision("Дело рассмотрено. Вынесен частичный вердикт в пользу истца.")

    # Печатаем краткую информацию об объекте
    print(case)  # вызовет __str__ и покажет сводку
    # Печатаем подробности
    print("Вердикт:", case.verdict)
    print("Слушания:", case.listening_datetimes)
    print("Участники:", case.case_participants)
