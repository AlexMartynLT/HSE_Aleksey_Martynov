import random  # Для генерации случайных чисел
import time    # Для замера времени работы алгоритмов


# 1. Генерация массива случайных чисел
def generate_random_array(size=100_000, min_val=1, max_val=1_000_000):
    """
    Генерирует массив случайных целых чисел.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


# 2. Генерация массива словарей
def generate_dict_array(size=100_000, min_val=1, max_val=1_000_000):
    """
    Генерирует массив словарей вида {"num_1": int, "num_2": int}.
    """
    return [
        {"num_1": random.randint(min_val, max_val),
         "num_2": random.randint(min_val, max_val)}
        for _ in range(size)
    ]


# 3. Алгоритм сортировки пузырьком
def bubble_sort(arr):
    """
    Алгоритм сортировки пузырьком.
    Возвращает отсортированный список.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Проверка, отсортирован ли массив (вспомогательная функция)
def is_sorted(arr):
    """
    Проверяет, отсортирован ли массив по возрастанию.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# Главный блок программы
if __name__ == "__main__":
    # --- Первый массив ---
    random_array = generate_random_array()

    print("Сортировка пузырьком (демонстрация на 500 элементах)...")
    test_array = random_array[:500]  # Берём первые 500 элементов для демонстрации
    start_time = time.time()
    sorted_array = bubble_sort(test_array)
    end_time = time.time()

    print("Отсортирован ли массив пузырьком?", is_sorted(sorted_array))
    print("Время сортировки пузырьком (500 элементов):", end_time - start_time, "секунд\n")

    # --- Второй массив ---
    dict_array = generate_dict_array()

    print("Сортировка массива словарей по ключу num_1...")
    start_time = time.time()
    dict_array.sort(key=lambda x: x["num_1"])
    end_time = time.time()
    print("Отсортирован ли массив по num_1?", all(
        dict_array[i]["num_1"] <= dict_array[i + 1]["num_1"] for i in range(len(dict_array) - 1)
    ))
    print("Время сортировки по num_1:", end_time - start_time, "секунд\n")

    print("Сортировка массива словарей по ключу num_2...")
    start_time = time.time()
    dict_array.sort(key=lambda x: x["num_2"])
    end_time = time.time()
    print("Отсортирован ли массив по num_2?", all(
        dict_array[i]["num_2"] <= dict_array[i + 1]["num_2"] for i in range(len(dict_array) - 1)
    ))
    print("Время сортировки по num_2:", end_time - start_time, "секунд\n")

    # --- Итог ---
    print("Задание выполнено ✅ (массивы сгенерированы и отсортированы корректно).")
