import random  # Модуль random нужен для генерации случайных чисел
import time    # Модуль time нужен для замера времени работы функций


# Функция для генерации отсортированного массива
def generate_sorted_array():
    """
    Генерирует массив чисел от 10 до 250_000_000
    со случайным шагом от 3 до 5.
    """
    step = random.randint(3, 5)  # Случайный шаг между элементами
    # range(start=10, stop=250_000_000, step=step) создаёт отсортированную последовательность
    return list(range(10, 250_000_000, step))


# Функция для генерации 10 случайных чисел
def generate_random_numbers():
    """
    Генерирует список из 10 случайных чисел
    в пределах от 10 до 250_000_000.
    """
    return [random.randint(10, 250_000_000) for _ in range(10)]


# Функция линейного поиска
def linear_search(arr, target):
    """
    Алгоритм линейного поиска.
    Последовательно перебирает элементы массива.
    Если находит target, возвращает индекс, иначе -1.
    """
    for index, value in enumerate(arr):  # Перебор с индексами
        if value == target:  # Если элемент равен искомому
            return index
    return -1  # Если число не найдено


# Функция бинарного поиска
def binary_search(arr, target):
    """
    Алгоритм бинарного поиска.
    Работает только с отсортированными массивами.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    left = 0  # Левая граница поиска
    right = len(arr) - 1  # Правая граница поиска

    while left <= right:  # Пока границы не пересеклись
        mid = (left + right) // 2  # Находим середину массива
        if arr[mid] == target:  # Если элемент найден
            return mid
        elif arr[mid] < target:  # Если искомое число больше середины
            left = mid + 1  # Сдвигаем левую границу вправо
        else:  # Если искомое число меньше середины
            right = mid - 1  # Сдвигаем правую границу влево
    return -1  # Если число не найдено


# Главный блок программы
if __name__ == "__main__":
    # 1. Генерируем массив
    sorted_array = generate_sorted_array()

    # 2. Генерируем 10 случайных чисел
    random_numbers = generate_random_numbers()

    print("Случайные числа для поиска:", random_numbers)

    # 3. Проверяем линейный поиск
    start_time = time.time()  # Засекаем время начала
    for number in random_numbers:
        result = linear_search(sorted_array, number)
        # Выводим результат поиска (найден или нет)
        print(f"Линейный поиск: число {number} найдено на позиции {result}")
    end_time = time.time()  # Засекаем время окончания
    print("Время линейного поиска:", end_time - start_time, "секунд\n")

    # 4. Проверяем бинарный поиск
    start_time = time.time()
    for number in random_numbers:
        result = binary_search(sorted_array, number)
        print(f"Бинарный поиск: число {number} найдено на позиции {result}")
    end_time = time.time()
    print("Время бинарного поиска:", end_time - start_time, "секунд")
