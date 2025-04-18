# Функция для вычисления факториала числа
def factorial(n):
    """Возвращает факториал числа n. Факториал — это произведение всех натуральных чисел от 1 до n."""
    result = 1
    for i in range(1, n + 1):
        result *= i  # Умножаем текущий результат на i
    return result

# Функция для поиска наибольшего числа из трёх
def max_of_three(numbers):
    """Возвращает наибольшее число из переданного кортежа numbers."""
    return max(numbers)  # Используем встроенную функцию max()

# Функция для расчёта площади прямоугольного треугольника
def triangle_area(a, b):
    """Возвращает площадь треугольника по двум катетам a и b. Формула: (a * b) / 2."""
    return (a * b) / 2

# Примеры использования функций
print("Факториал 5 =", factorial(5))  # Выведет 120
print("Наибольшее из (10, 5, 8) =", max_of_three((10, 5, 8)))  # Выведет 10
print("Площадь треугольника с катетами 3 и 4 =", triangle_area(3, 4))  # Выведет 6.0
