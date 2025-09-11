# Импортируем datetime, чтобы работать с датой и временем (например, когда судья назначает слушание).
from datetime import datetime

# Создаём класс Judge — он будет описывать судью.
class Judge:
    """Класс, описывающий судью, который ведёт судебные дела."""

    # Метод-конструктор __init__ вызывается при создании судьи.
    def __init__(self, full_name, court_name):
        # full_name — ФИО судьи (например, "Иванов Иван Иванович").
        self.full_name = full_name
        # court_name — название суда (например, "Арбитражный суд г. Москвы").
        self.court_name = court_name
        # current_cases — список дел, которые находятся в производстве у судьи.
        self.current_cases = []
        # finished_cases — список завершённых дел.
        self.finished_cases = []

    # Метод для добавления дела в список текущих дел судьи.
    def assign_case(self, case):
        # Добавляем дело в список текущих дел.
        self.current_cases.append(case)
        # Возвращаем True, чтобы показать успешное добавление.
        return True

    # Метод для назначения слушания по делу.
    def schedule_hearing(self, case, dt, location):
        # Проверяем, есть ли это дело в списке текущих.
        if case not in self.current_cases:
            print("Дело не найдено у данного судьи!")
            return False

        # Добавляем слушание через метод дела.
        case.set_a_listening_datetime(dt, location=location, note=f"Назначено судьёй {self.full_name}")
        print(f"Судья {self.full_name} назначил слушание по делу {case.case_number} на {dt} в {location}")
        return True

    # Метод для вынесения решения по делу.
    def make_decision(self, case, verdict_text):
        # Проверяем, что дело действительно есть у этого судьи.
        if case not in self.current_cases:
            print("Дело не найдено у данного судьи!")
            return False

        # Выносим решение через метод дела.
        case.make_a_decision(verdict_text)

        # Убираем дело из текущих и переносим его в завершённые.
        self.current_cases.remove(case)
        self.finished_cases.append(case)

        print(f"Судья {self.full_name} вынес решение по делу {case.case_number}.")
        return True

    # Удобное строковое представление судьи (при печати объекта).
    def __str__(self):
        return (
            f"Judge(full_name={self.full_name}, "
            f"court_name={self.court_name}, "
            f"current_cases={len(self.current_cases)}, "
            f"finished_cases={len(self.finished_cases)})"
        )


# Пример использования класса:
if __name__ == "__main__":
    # Чтобы протестировать, создадим судью и дело.
    # Для этого импортируем класс CourtCase из предыдущего задания (если он в том же файле, то просто используем).
    from datetime import datetime

    # Берём готовый CourtCase из прошлого ДЗ
    class CourtCase:
        def __init__(self, case_number):
            self.case_number = case_number
            self.case_participants = []
            self.listening_datetimes = []
            self.is_finished = False
            self.verdict = ""

        def set_a_listening_datetime(self, dt, location=None, note=None):
            self.listening_datetimes.append({"datetime": dt, "location": location, "note": note})

        def make_a_decision(self, verdict_text):
            self.verdict = verdict_text
            self.is_finished = True

    # Создаём судью
    judge = Judge("Иванов Иван Иванович", "Арбитражный суд г. Москвы")

    # Создаём дело
    case1 = CourtCase("А-456/2025")

    # Назначаем дело судье
    judge.assign_case(case1)

    # Судья назначает слушание
    judge.schedule_hearing(case1, "2025-09-20 11:00", "Зал №3")

    # Судья выносит решение
    judge.make_decision(case1, "Дело закрыто. Иск удовлетворён.")

    # Печатаем информацию о судье
    print(judge)
    # Печатаем информацию о деле
    print("Вердикт по делу:", case1.verdict)
